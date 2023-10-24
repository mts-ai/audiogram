# Установите зависимости

```
pip install grpcio==1.56.2
pip install grpcio-tools==1.56.2
pip install python-keycloak==3.3.0
```

# Сгенерируйте код gRPC

`python3 -m grpc_tools.protoc -I . --python_out=.  --grpc_python_out=. tts.proto`

# Запустите код примеров

## Файловый режим
`python3 synthesize_file.py "Синтез и распознавание речи являются одной из основных областей, в которых применяется искусственный интеллект."`

## Потоковый режим
`python3 synthesize_stream.py "Синтез и распознавание речи являются одной из основных областей, в которых применяется искусственный интеллект."`