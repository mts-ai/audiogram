
# Общая информация

**Audiogram** – это сервис на базе нейронных сетей и методов машинного обучения для озвучивания текстов и преобразования речи в текст. В состав сервиса входят 2 модуля:

* **ASR** (Automatic Speech Recognition) – отвечает за конвертацию речи в текст

* **TTS** (Text To Speech) – отвечает за синтез речи

Audiogram можно использовать для самых разнообразных задач – создания голосовых помощников, роботов для колл-центров, транскрибирования и последующего анализа звонков и других звуковых записей, озвучки текста, создания субтитров и многого другого.

Администрирование сервиса производится через **веб-клиент**, который позволяет просматривать и редактировать данные текущих пользователей, добавлять клиентов, изменять настройки синтеза и распознавания речи, а также просматривать статистику использования сервиса.

В данном руководстве описывается как выполнять эти действия.

# Начало работы

Для начала работы вам необходимо авторизоваться. Откройте адрес веб-клиента в браузере и введите данные учетной записи.

Если учетные данные введены верно, выполняется вход в сервис.

![Основное окно веб-клиента Audiogram](/images/wc_main_window.png)

# Функции администратора

При входе в веб-клиент по умолчанию открывается **Панель управления клиентами**. На ней находится список всех зарегистрированных пользователей.

Вы можете просматривать информацию о клиентах, менять настройки использования Audiogram, смотреть личную статистику и т.д. Более подробно эти действия описаны в следующей секции.



В левой части экрана находится боковая панель. С её помощью вы можете:

* вернуться на панель управления клиентами с других страниц веб-клиента

* добавить клиента

* выйти из учетной записи

## Управление клиентами

Управление клиентами Audiogram производится через панель, на которую администратор попадает при входе в веб-клиент. На этой панели вы можете:

* посмотреть / отредактировать информацию о клиенте

* заблокировать / разблокировать клиента

* посмотреть / изменить настройки использования Audiogram

* посмотреть статистику

### Просмотр / изменение информации о клиенте

Основная информация представлена в списке клиентов, который находится на панели управления:



Список состоит из трех столбцов:

* **ID** – ID клиента

* **Компания** – название компании

* **Статус** – статус клиента относительно сервиса Audiogram (Active – активный; Inactive – заблокированный)

Для просмотра подробной информации наведите указатель мыши на клиента и один раз нажмите левую кнопку. Произойдет переход на страницу выбранного клиента.

На странице можно посмотреть статус клиента, ID клиента, название компании, текущие настройки синтеза и распознавания речи, а также статистику использования Audiogram.

Разделы с названием компании и настройками синтеза / распознавания речи можно редактировать. Для этого воспользуйтесь кнопкой:



### Блокировка / разблокировка клиента

Если вам необходимо заблокировать или разблокировать клиента, выберите его на панели управления и нажмите соответствующую кнопку:



### Просмотр / редактирование настроек использования Audiogram

Для просмотра и редактирования текущих настроек синтеза (TTS) и распознавания (ASR) речи выберите клиента на панели управления и прокрутите страницу вниз до раздела **Опции**.



Чтобы изменить настройки, воспользуйтесь кнопкой:



Внесите необходимые коррективы и нажмите **Сохранить**.

### Просмотр статистики по клиенту

Чтобы посмотреть, как клиент пользуется услугами сервиса Audiogram, выберите клиента на панели управления и прокрутите страницу вниз до раздела **Статистика**. Укажите временной интервал, статистику за который вы хотите получить.

В разделе **ASR** (AutomaticSpeechRecognition) будет представлена статистика по преобразованию речи в текст:



Раздел **TTS** (Text to Speech) содержит статистику по переводу текста в речь:



Статистические данные можно скачать в файл формата .csv. Для этого нажмите **Скачать CSV**.

## Добавление клиента

Чтобы добавить клиента, нажмите соответствующую кнопку в левой части экрана. Откроется страница, на которой необходимо ввести информацию о новом клиенте:



Все поля заполняются вручную. Для завершения ввода нажмите **Добавить**.

# Завершение работы

Для завершения работы нажмите **Выйти** в левом нижнем углу экрана.