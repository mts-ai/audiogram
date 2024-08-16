# Audiogram

Audiogram - это сервис, оказывающий услуги по синтезу и распознаванию речи.

В данном репозитории хранятся:

* [публичный proto-файл для распознавания речи](https://github.com/mts-ai/audiogram/blob/main/asr/v3/stt_v3.proto);

* [публичный proto-файл для синтеза речи](https://github.com/mts-ai/audiogram/blob/main/tts/v2/tts.proto);
* примеры кода клиентских приложений для распознавания речи:  
  
  **Внимание!** Следующие примеры клиентов для распознавания речи создавались [для предыдущей версии stt.proto файла](https://github.com/mts-ai/audiogram/blob/main/asr/v2/stt.proto). Обновленные примеры для [stt_v3.proto](https://github.com/mts-ai/audiogram/blob/main/asr/v3/stt_v3.proto) находятся в разработке.

     * Python3: [распознавание в файловом режиме](https://github.com/mts-ai/audiogram/blob/main/asr/v2/python3/recognize_file.py); [распознавание в потоковом режиме](https://github.com/mts-ai/audiogram/blob/main/asr/v2/python3/recognize_stream.py).

* примеры кода клиентских приложений для синтеза речи:

     * Python3: [синтез в файловом режиме](https://github.com/mts-ai/audiogram/blob/main/tts/v2/python3/synthesize_file.py); [синтез в потоковом режиме](https://github.com/mts-ai/audiogram/blob/main/tts/v2/python3/synthesize_stream.py).