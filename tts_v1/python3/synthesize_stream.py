import argparse
import random
from configparser import ConfigParser
from pprint import pprint
from typing import Mapping
import wave

import grpc
from google.protobuf.json_format import MessageToDict
from keycloak import KeycloakOpenID

import tts_pb2
import tts_pb2_grpc


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


def synthesize_stream(text: str, api_address: str, auth_config: Mapping[str, str]):
    sample_rate = 22050
    request = tts_pb2.SynthesizeSpeechRequest(
        text=text,
        encoding=tts_pb2.AudioEncoding.LINEAR_PCM,
        sample_rate_hertz=sample_rate,
        voice_name="gandzhaev",
        synthesize_options=tts_pb2.SynthesizeOptions(
            postprocessing_mode=tts_pb2.SynthesizeOptions.PostprocessingMode.POST_PROCESSING_DISABLE,
            model_type="default",
            voice_style=tts_pb2.VoiceStyle.VOICE_STYLE_NEUTRAL,
        ),
    )
    print("Prepared request:")
    pprint(MessageToDict(request))

    options = [
        ("grpc.min_reconnect_backoff_ms", 1000),
        ("grpc.max_reconnect_backoff_ms", 1000),
        ("grpc.max_send_message_length", -1),
        ("grpc.max_receive_message_length", -1),
    ]

    credentials = grpc.ssl_channel_credentials()

    print(f"\nSending request to gRPC server {api_address}")

    with grpc.secure_channel(
        api_address, credentials=credentials, options=options
    ) as channel:
        stub = tts_pb2_grpc.TTSStub(channel)

        request_metadata = get_request_metadata(auth_config)

        response_iterator = stub.StreamingSynthesize(
            request,
            metadata=request_metadata,
            wait_for_ready=True,
        )

        print("Call initial metadata:")
        initial_metadata = dict(response_iterator.initial_metadata())
        print(f"request_id={initial_metadata.get('request_id', '')}")
        print(f"trace_id={initial_metadata.get('external_trace_id', '')}")

        path = "synthesized_audio.wav"
        wave_data = wave.open(path, "wb")
        wave_data.setnchannels(1)
        wave_data.setframerate(sample_rate)
        wave_data.setsampwidth(2)

        for idx, chunk in enumerate(response_iterator, 1):
            print(f"Received chunk #{idx} of {len(chunk.audio)} bytes")
            wave_data.writeframesraw(chunk.audio)

        print(f"Saved received audio to {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, help="text for speech synthesis")

    args = parser.parse_args()

    config = read_api_config()

    synthesize_stream(
        args.text,
        config["API"]["server_address"],
        config["Auth"],
    )
