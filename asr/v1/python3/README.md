# Установите зависимости

```
pip install grpcio==1.56.2
pip install grpcio-tools==1.56.2
pip install python-keycloak==3.3.0
```

# Сгенерируйте код gRPC

`python3 -m grpc_tools.protoc -I . --python_out=.  --grpc_python_out=. stt.proto`

# Запустите код примеров

## Файловый режим
`python3 recognize_file.py ./test.wav`

## Потоковый режим
`python3 recognize_stream.py ./test.wav`