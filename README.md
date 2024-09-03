# Audiogram

Audiogram - это сервис, оказывающий услуги по синтезу и распознаванию речи.

В данном репозитории хранятся:

* [руководство по эксплуатации Audiogram](https://github.com/mts-ai/audiogram/blob/main/AG_manual_ru.md);

* [публичный proto-файл для распознавания речи](https://github.com/mts-ai/audiogram/blob/main/asr/v3/stt_v3.proto);

* [публичный proto-файл для синтеза речи](https://github.com/mts-ai/audiogram/blob/main/tts/v2/tts.proto);

* [примеры кода клиентских приложений](https://github.com/mts-ai/audiogram/tree/main/demo_clients)  
  
  **Внимание!** Эти примеры создавались для [stt_v3.proto](https://github.com/mts-ai/audiogram/blob/main/asr/v3/stt_v3.proto) и [tts_v2.proto](https://github.com/mts-ai/audiogram/blob/main/tts/v2/tts.proto)  
  В качестве образцов кода клиентских приложений [для предыдущей версии stt.proto файла](https://github.com/mts-ai/audiogram/blob/main/asr/v2/stt.proto) используйте следующие примеры:

     * [распознавание в файловом режиме](https://github.com/mts-ai/audiogram/blob/main/asr/v2/python3/recognize_file.py)
     * [распознавание в потоковом режиме](https://github.com/mts-ai/audiogram/blob/main/asr/v2/python3/recognize_stream.py)