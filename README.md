# telegram-bot-SMTP-work-example - Телеграм-бот, принимающий и отправляющий сообщения через SMTP яндекса на указанный почтовый ящик
Телеграм-бот, который принимает email адрес, введенный пользователем и сообщение, которое необходимо отправить и отправляет его на указанный в переменной окружения почтовый ящик через SMTP Яндекса. <br>
## Стек
- Python 3.10 <br>
- smtplib (библиотека для работа с SMTP) <br>
- aiogram (для разработки телеграм-бота) <br>
## Использование:
1. Клонируйте репозиторий: <br>
```git clone https://github.com/evgeshkins/telegram-bot-SMTP-work-example.git . ``` <br>
2. Создайте виртуальное окружение: <br>
```python -m venv venv``` <br>
либо <br>
```py -m venv venv``` <br>
3. Активируйте виртуальное окружение: <br>
На Windows: <br>
```.venv\Scripts\activate``` <br>
На Linux: <br>
```source venv/bin/activate``` <br>
4. Установите библиотеки: <br>
```pip install -r requirements.txt``` <br>
5. Создайте файл .env в корне проекта и внесите туда значения следующих переменных: <br>
```python
BOT_TOKEN="значение токена для бота"
SMTP_EMAIL="email, на который будут присылаться сообщения"
SMTP_PASSWORD="пароль от SMTP"
SMTP_SERVER="адрес SMTP-сервера"
SMTP_PORT="порт SMTP (писать без кавычек)"
```
*Значение токена для бота можно получить у бота BotFather в телеграм. <br>
**Как получить пароль от SMTP Яндекса можно узнать в этой документации: https://yandex.ru/support/yandex-360/customers/mail/ru/mail-clients/others.html <br>
6. Запустите скрипт:
```python
python bot.py
```
7. Проверьте работоспособность через телеграм-бота <br>
### ВАЖНО! Если устанавливаете библиотеки не через requirements.txt, то необходимо установить aiogram версии 2.x!
### Также, проверяйте спам, сообщение может оказаться там.
