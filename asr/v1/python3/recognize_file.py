import argparse
import random
from configparser import ConfigParser
from pprint import pprint
from typing import Mapping

import grpc
from google.protobuf.json_format import MessageToDict
from keycloak import KeycloakOpenID

import stt_pb2
import stt_pb2_grpc


def read_api_config(file_name: str = "config.ini") -> ConfigParser:
    """
    Загружает параметры соединения с API и авторизации из ini-файла.
    Структура файла и примеры значений:

    [API]
    server_address: audiogram.mts.ai:443

    [Auth]
    sso_server_url: https://isso.mts.ru/auth/
    realm_name: mts
    client_id: <client id>
    client_secret: <client secret>
    """

    config = ConfigParser()
    config.read(file_name)

    return config


def make_va_config() -> stt_pb2.VoiceActivityConfig:
    vad_options = stt_pb2.VADOptions(
        threshold=0.2,
        speech_pad_ms=300,
        min_silence_ms=100,
        min_speech_ms=250,
        mode=stt_pb2.VADOptions.VAD_MODE_DEFAULT,
    )
    result = stt_pb2.VoiceActivityConfig(
        usage=stt_pb2.VoiceActivityDetectionAlgorithmUsage.USE_VAD,
        vad_options=vad_options,
    )
    return result


def make_recognition_config() -> stt_pb2.RecognitionConfig:
    options = {
        "va_config": make_va_config(),
        "va_response_mode": stt_pb2.VoiceActivityMarkEventsMode.VA_ENABLE_ASYNC,
        "enable_genderage": True,
    }
    result = stt_pb2.RecognitionConfig(**options)

    result.encoding = stt_pb2.AudioEncoding.LINEAR_PCM
    result.sample_rate_hertz = 8000
    result.audio_channel_count = 1
    result.enable_word_time_offsets = True
    result.max_alternatives = 3

    result.model = "e2e-v1"
    result.language_code = "ru"

    return result


def get_request_metadata(auth_config: Mapping[str, str]) -> list[tuple[str, str]]:
    sso_connection = KeycloakOpenID(
        auth_config["sso_server_url"],
        auth_config["realm_name"],
        auth_config["client_id"],
        auth_config["client_secret"],
        verify=True,
    )
    token_info = sso_connection.token(grant_type="client_credentials")
    access_token = token_info["access_token"]

    trace_id = str(random.randint(1000, 9999))
    print(f"Trace id: {trace_id}")

    metadata = [
        ("authorization", f"Bearer {access_token}"),
        ("external_trace_id", trace_id),
    ]

    return metadata


def recognize_file(path: str, api_address: str, auth_config: Mapping[str, str]):
    with open(path, "rb") as f:
        audio = f.read()

    recognition_config = make_recognition_config()
    print("Using recognition config:")
    pprint(recognition_config)

    request = stt_pb2.RecognizeRequest(
        config=recognition_config, audio_content=stt_pb2.RecognitionAudio(audio=audio)
    )

    options = [
        ("grpc.min_reconnect_backoff_ms", 1000),
        ("grpc.max_reconnect_backoff_ms", 1000),
        ("grpc.max_send_message_length", -1),
        ("grpc.max_receive_message_length", -1),
    ]

    credentials = grpc.ssl_channel_credentials()

    print(f"Sending request to gRPC server {api_address}")

    with grpc.secure_channel(
        api_address, credentials=credentials, options=options
    ) as channel:
        stub = stt_pb2_grpc.STTStub(channel)

        request_metadata = get_request_metadata(auth_config)

        response, call = stub.Recognize.with_call(
            request,
            metadata=request_metadata,
            wait_for_ready=True,
        )

        print("Received response:")
        initial_metadata = dict(call.initial_metadata())
        print(f"request_id={initial_metadata.get('request_id', '')}")
        print(f"trace_id={initial_metadata.get('external_trace_id', '')}")
        pprint(MessageToDict(response))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="path to an audio file")

    args = parser.parse_args()

    config = read_api_config()

    recognize_file(
        args.path,
        config["API"]["server_address"],
        config["Auth"],
    )
