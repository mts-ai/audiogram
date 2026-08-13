# Как подключиться к демо-стенду

# Запрос доступа к демо-клиенту

1. Менеджер запрашивает доступ у PO к демо-стенду **grpc.audiogram-demo.mts.ai**, предварительно подписав NDA с клиентом.
2. PO создает задачу на DevOps в которой указывает (ФИО ответственного от Заказчика, рабочая почта, телеграм (опционально) и телефон, срок до которого активен доступ. Все предоставляется менеджером).
3. DevOps присылает клиент и секрет.
4. PO архивирует с паролем клиент и секрет и передает менеджеру.
5. Менеджер передает инструкцию по подключению к демо-клиенту Audiogram почтой с запароленным архивом. Пароль от архива пересылает личным сообщением в телеграм или другим способом, но лично клиенту.

# Использование демо-клиента

Распакуйте архив с демо-клиентом в пустую директорию и следуйте инструкциям ниже. Демо-клиент можно скачать по ссылке: https://github.com/mts-ai/audiogram/tree/main/demo_clients

## Шаг 1. Подготовьте окружение

1. Откройте Терминал (или cmd в Windows).
2. Установите любую версию Python 3.11. Например, 3.11.6
   >  ВНИМАНИЕ:  C более поздними версиями Python возможны ошибки при установке зависимостей.

3. Проверьте установленную версию Python и убедитесь, что у вас стоит Python 3.11.

    ``` windows 
    $ python --version
    ```
4. Перейдите в папку с демо-клиентом и откройте файл **FAG_config.ini** в текстовом редакторе и сделайте следующие изменения:
    1) Найдите секцию **# Keycloak authentication credentials (ID and secret)**.
    2) Введите свои значения в параметрах **client_id** и **client_secret**. Их можно получить по запросу у DevOps Audiogram.
5. В Терминале (или cmd в Windows), перейдите в директорию, в которой вы распаковали архив и создайте Python virtual environment (venv):
     ``` windows 
      $ python -m venv .venv
      ```
6. Активируйте venv:
      ``` windows 
      $ .\.venv\Scripts\activate
      ```
7. Установите зависимости:
      ``` windows 
      $ pip install -r requirements.txt
      $ pip install -r requirements.audio_archive.txt
      ```

## Шаг 2. Запустите приложение

Вы можете получить краткую информацию о приложении, выполнив следующую команду:

    ``` windows 
    $ python -m clients.main --help
    ```

Вы также можете посмотреть детальную документацию по командам в директории ./docs/.

# Пример 1 - Файловое распознaвание голоса

1. Проверьте, что вы находитесь в virtual environment в директории, где вы производили установку и выполните следующую команду:

      ``` windows 
      $ python -m clients.main recognize file --audio-file {path/to/file.wav} --config FAG_config.ini
      ```
2. Команда выведет результат на экран.

    ``` windows 
    Loading .ini configuration from "FAG_config.ini"
    
    Fetching SSO access token...
    
    Request parameters:
    Audio sample rate: 22050
    Audio channels: 1
    VAD algorithm: VAD
    Genderage enabled: False
    Punctuator enabled: False
    Denormalization enabled: False
    Speaker labeling enabled: False
    Word time offsets enabled: False
    Antispoofing enabled: False
    Split by channel: False
    
    Connecting to gRPC server - grpc.audiogram-demo.mts.ai:443
    
    Response metadata:
    date: 'Thu, 18 Jun 2026 21:18:42 GMT'
    request_id: 'FR-2c17c0e4-d99f-4fc4-97d4-633deb072472'
    request-id: '2c17c0e4-d99f-4fc4-97d4-633deb072472'
    client_id: ' '
    strict-transport-security: 'max-age=31536000; includeSubDomains'
    
    Result 1:
    Channel: 1
    Hypothesis (00.00s-13.59s): "команда мтс эй яй разработала сервис способный озвучить любой текст одним из четырёх голосов напишите здесь то что хотите услышать остальное мы сделаем сами объём текста до тысячи знаков" is_final: True, confidence: 0
    ```

Это самый простой вариант данной команды, использующий параметры по умолчанию. Команду можно расширить, передав дополнительные параметры. Все имеющиеся параметры с детальным описанием можно найти в файлах **text-doc-en.txt** или **text-doc-ru.txt** в директории ./docs/. Ищите разделы "===== Опции для распознавания голоса (SR_OPTIONS) =====" и "===== Опции файлового распознавания голоса (SR_FILE_OPTIONS) =====".    

# Пример 2 - Файловое распознавание голоса с дополнительными параметрами

В данном примере добавлены параметры для распознавания пола, возраста и эмоции говорящего, а так же определения спуфинг-атаки.

1. Проверьте, что вы находитесь в virtual environment в директории, где вы производили установку и выполните следующую команду:


   ``` windows 
    $ python -m clients.main recognize file --audio-file {path/to/file.wav} --config FAG_config.ini --enable-genderage --enable-antispoofing
   ```
2. Команда выведет результат на экран.   

    ``` windows 
    Loading .ini configuration from "FAG_config.ini"
    
    Fetching SSO access token...
    
    Request parameters:
    Audio sample rate: 22050
    Audio channels: 1
    VAD algorithm: VAD
    Genderage enabled: True
    Punctuator enabled: False
    Denormalization enabled: False
    Speaker labeling enabled: False
    Word time offsets enabled: False
    Antispoofing enabled: True
    Split by channel: False
    
    Connecting to gRPC server - grpc.audiogram-demo.mts.ai:443
    
    Response metadata:
    date: 'Thu, 18 Jun 2026 21:26:45 GMT'
    request_id: 'FR-5f57880d-2a10-44c2-98a4-9b9b338a1c19'
    request-id: '5f57880d-2a10-44c2-98a4-9b9b338a1c19'
    client_id: ''
    strict-transport-security: 'max-age=31536000; includeSubDomains'
    
    Result 1:
            Channel: 1
            Hypothesis (00.00s-13.59s): "команда мтс эй яй разработала сервис способный озвучить любой текст одним из четырёх голосов напишите здесь то что хотите услышать остальное мы сделаем сами объём текста до тысячи знаков" is_final: True, confidence: 0
            Genderage result:
                    gender: GENDER_UNDEF
                    age: AGE_CHILD
                    emotion:
                            positive=0.015
                            neutral=0.096
                            negative_angry=0.889
                            negative_sad=0.000
            Spoofing results:
                    Result: ATTACK_DETECTED
                    Confidence: 0.9721
                    Interval: 0.0s - 5.0s
   ```
# Использование API Audiogram   

Подробно с публичной документацией Audiogram вы можете ознакомиться по ссылке: https://github.com/mts-ai/audiogram/blob/main/AG_manual_ru.md

1. Получите access_token, в Postman или с помощью командной строки и команды curl:

   ``` windows 
    curl -X POST "https://sso.dev.mts.ai/realms/audiogram-demo/protocol/openid-connect/token" -d "client_id=CLIENT_ID" -d "client_secret=CLIENT_SECRET" -d "grant_type=client_credentials"
   ```

   В ответ вы получите:   

    ``` windows 
    {
        "access_token": "your_access_token",
        "expires_in": 300,
        "refresh_expires_in": 0,
        "token_type": "Bearer",
        "not-before-policy": 0,
        "scope": "profile email"
    }
   ```

2. Укажите Bearer Token. Например, в Postman. Создайте grps запрос. Перейдите на вкладку **Metadata**. В поле **key** ввeдите "authorization", а в поле **Value** -  "Bearer <access token>". 

   Также задайте  "x-ai-account" для **key** и "demo" для **value**.

3. Выполните запроc. Например: TTS/GetModelsInfo 

   Ответ на запрос:

   ``` windows 
    {
        "models": [
            {
                "name": "klukvin",
                "sample_rate_hertz": 8000,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "gandzhaev",
                "sample_rate_hertz": 8000,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "koryakina",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "gandzhaev",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "vostretsov",
                "sample_rate_hertz": 8000,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "vostretsov",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "klukvin",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "voice 2",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "eng voice"
            },
            {
                "name": "gavrilov",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "cloning"
            },
            {
                "name": "kishchik",
                "sample_rate_hertz": 8000,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "gavrilov",
                "sample_rate_hertz": 8000,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "borisova",
                "sample_rate_hertz": 8000,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "voice 1",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "eng voice"
            },
            {
                "name": "kishchik",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "borisova",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "eldarov",
                "sample_rate_hertz": 8000,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "eldarov",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "high_quality"
            },
            {
                "name": "voice 4",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "eng voice"
            },
            {
                "name": "voice 3",
                "sample_rate_hertz": 22050,
                "language_code": "",
                "type": "eng voice"
            },
            {
                "name": "koryakina",
                "sample_rate_hertz": 8000,
                "language_code": "",
                "type": "high_quality"
            }
        ],
        "header": {
            "timestamp": "1781820375432"
        }
    }
   ```