
# О сервисе и веб-клиенте Audiogram

**Audiogram** – это сервис на базе нейронных сетей и методов машинного обучения для озвучивания текстов и преобразования речи в текст.

Audiogram можно использовать для самых разнообразных задач – создания голосовых помощников, роботов для колл-центров, транскрибирования и последующего анализа звонков и других звуковых записей, озвучки текста, создания субтитров и многого другого.

Администрирование сервиса производится через **веб-клиент**, который позволяет добавлять бизнес-аккаунты, пользователей, настраивать права доступа к ресурсам Audiogram, а также просматривать статистику использования сервиса.

В данном руководстве описывается как выполнять эти действия.

# Начало работы

Для начала работы с веб-клиентом Audiogram откройте его адрес в любом браузере.

## Аутентификация

Пройдите аутентификацию:  
<image src="/images/iam.png">

## Выбор аккаунта

На экране отобразятся доступные вам аккаунты. Выберите в какой аккаунт необходимо зайти.
[screenshot]

Аккаунты могут быть двух видов:

* **сервис-аккаунт**: ассоциируется с компанией, которая является владельцем инсталляции Audiogram. Пользователи, включённые в сервис-аккаунт, обладают привилегированными уровнями доступа и имеют возможность определять права доступа к ресурсам и сущностям, которые закреплены за бизнес-аккаунтами. Для каждой инсталляции Audiogram может быть только один сервис-аккаунт; он создаётся в процессе развёртывания продукта.
 
* **бизнес-аккаунт**: ассоциируется с компанией, которой предоставляются услуги Audiogram. Пользователи, включённые в бизнес-аккаунт, имеют права доступа к ресурсам и сущностям, закреплённым за данным аккаунтом. Услугами одной инсталляции Audiogram могут пользоваться несколько бизнес-аккаунтов.

После входа в веб-клиент, вы можете переключаться между доступными аккаунтами при помощи меню в правом верхнем углу экрана:
[screenshot]

# Функции сервис-аккаунта

Выполнив вход в сервис-аккаунт, вы можете совершать следующие действия:

* посмотреть список доступных бизнес-аккаунтов;
* посмотреть и при необходимости изменить название конкретного бизнес-аккаунта;
* добавить бизнес-аккаунт;
* заблокировать/разблокировать бизнес аккаунт;
* удалить бизнес-аккаунт.

## Просмотр доступных бизнес-аккаунтов

При входе в сервис-аккаунт отображается список доступных бизнес-аккаунтов:
[screenshot]
**Примечание**: при первом входе в сервис-аккаунт список доступных бизнес-аккаунтов будет пустым.

Используя меню в правом нижнем углу, можно выбрать какое количество бизнес-аккаунтов будет отображаться на странице:
[screenshot]

Чтобы найти интересующий вас аккаунт, прокрутите список вниз или воспользуйтесь поиском:
[screenshot]

## Просмотр информации и изменение названия бизнес-аккаунта

Если необходимо посмотреть дату создания или изменить название бизнес-аккаунта, нажмите его название в общем списке бизнес-аккаунтов:
[screenshot]

Для изменения названия воспользуйтесь иконкой **Редактировать** [screenshot]

## Добавление бизнес-аккаунта

Чтобы добавить бизнес-аккаунт, нажмите **Добавить аккаунт**:
[screenshot]

В открывшемся окне заполните следующие поля:
[screenshot]
* **Название**:
* **Логин**:
* **Имя администратора**:
* **Идентификатор администратора**:  
После заполнения всех полей нажмите **Создать аккаунт**.

## Блокировка/разблокировка бизнес-аккаунта

Если необходимо заблокировать или разблокировать бизнес-аккаунт, воспользуйтесь переключателем:  
[screenshot]

## Удаление бизнес-аккаунта

Для того, чтобы удалить бизнес-аккаунт, выполните одно из следующих действий:
* нажмите иконку корзины [screenshot] справа от переключателя блокировки/разблокировки аккаунта;
* нажмите на бизнес-аккаунт, который хотите удалить, и выберите **Удалить аккаунт**.

# Функции бизнес-аккаунта

Выполнив вход в бизнес-аккаунт, вы можете совершать следующие действия:

* посмотреть информацию об этом аккаунте;
* посмотреть список пользователей;
* добавить пользователя;
* заблокировать/разблокировать пользователя;
* изменить имя пользователя или его настройки доступа к ресурсам и сущностям Audiogram;
* посмотреть и выгрузить статистику использования Audiogram.

## Просмотр информации о бизнес-аккаунте

При входе в бизнес-аккаунт можно посмотреть общую информацию об этом аккаунте:  
[screenshot]

## Просмотр списка пользователей

Под пользователем Audiogram подразумевается человек или приложение, которое присылает запросы на синтез или распознавание речи.

Для того, чтобы посмотреть какие пользователи относятся к данному бизнес-аккаунту, перейдите на вкладку **Доступы**:  
[screenshot]
Физические пользователи отображаются на вкладке **Пользователи**, а пользователи типа "программы" - на вкладке **Приложения**.

Используя меню в правом нижнем углу, можно выбрать какое количество пользователей будет отображаться на странице:  
[screenshot]

Чтобы найти интересующего вас пользователя прокрутите список вниз или воспользуйтесь поиском:  
[screenshot]

## Добавление пользователя

Чтобы добавить пользователя, выполните одно из следующих действий:

* если необходимо добавить физического пользователя, в разделе **Пользователи** нажмите **Добавить пользователя**
* если необходимо добавить пользователя типа "программа", в разделе **Приложения** нажмите **Добавить приложение**

Далее введите данные о пользователе и предоставьте необходимые права:  
[screenshot]  

1. Если тип пользователя "программа", введите её название и ID. Если это физический пользователь, введите его ID и имя.
2. Выберите какие права будут предоставлены пользователю:
* **Администрирование**: при выборе этой опции пользователь будет иметь возможность заходить в веб-клиент Audiogram.
* **Чтение из аудиоархива**: при выборе этой опции пользователь будет иметь возможность скачивать аудио, поступившие на распознавание, и результаты распознавания из аудиоархива.
* **Доступ к статистике**: при выборе этой опции пользователь будет иметь доступ к статистике использования Audiogram.
* **Распознавание речи**: в этом разделе выберите какие режимы распознавания будут доступны пользователю. Есть 2 режима:
     * **потоковый** - в этом режиме клиент устанавливает соединение с Audiogram и присылает аудио на распознавание чанками (по кусочкам). Обработка аудио проходит по мере поступления и заканчивается, когда клиент закрывает соединение.
     * **файловый** (**синхронный**) - в этом случае клиент присылает аудиофайл на распознавание, Audiogram в ответе отправляет результаты распознавания и закрывает соединение.<br />  
     При выборе любого из режимов появляются дополнительные опции:  
     * **Запись в аудиоархив**: при выборе этой опции аудио, поступившее на распознавание, и результаты распознавания будут сохраняться в аудиоархив.  
     * **Модель**: выберите в этом меню какие ML-модели, осуществляющие распознавание, будут доступны пользователю.
* **Синтез речи**: в этом разделе выберите какие режимы распознавания будут доступны пользователю. Есть 2 режима:
     * **потоковый** - в этом режиме клиент устанавливает соединение с Audiogram и присылает текст на озвучку частями. Синтез речи проходит по мере поступления текста и заканчивается, когда клиент закрывает соединение.
     * **файловый** (**синхронный**) - в этом случае клиент присылает текст на синтез, Audiogram в ответе отправляет результаты озвучки и закрывает соединение.<br />  
     При выборе любого из режимов появляются дополнительная опция:
     * **Голоса**: выберите в этом меню какие голоса для синтеза будут доступны пользователю.

## Блокировка/разблокировка пользователя

Если необходимо заблокировать или разблокировать пользователя, воспользуйтесь переключателем:  
[screenshot]

## Изменение имени пользователя и его настроек доступа к ресурсам Audiogram

Чтобы изменить имя пользователя или его настройки доступа к ресурсам и сущностям Audiogram, нажмите имя пользователя в списке:  
[screenshot]

Для изменения имени воспользуйтесь иконкой **Редактировать** [screenshot]
Настройки доступа, отображающиеся в этом окне, совпадают с настройками, которые необходимо задать при добавлении пользователя. Они были описаны выше в секции **Добавление пользователя**.

## Просмотр и выгрузка статистики использования Audiogram

Для просмотра статистики использования Audiogram перейдите на вкладку **Статистика**.
Вы можете посмотреть статистику по всему бизнес-аккаунту:  
[screenshot]

или по клиентам:  
[screenshot]

Чтобы посмотреть статистику по определенному клиенту, нажмите его имя в списке:  
[screenshot]

Для выбора временного отрезка, статистику за который вы хотите посмотреть, воспользуйтесь формой в правом верхнем углу экрана.

Статистические данные использования Audiogram можно выгрузить в формате .csv. Для этого воспользуйтесь кнопкой [screenshot]

# Завершение работы
Для завершения работы нажмите на иконку аккаунта в правом верхнем углу и выберите **Выход**.  
[screenshot]