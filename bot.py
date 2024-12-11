import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from dotenv import load_dotenv
import os

load_dotenv()

# Конфигурация
BOT_TOKEN = os.getenv("BOT_TOKEN")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = 465
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Регулярное выражение для проверки email
EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Хранение состояния пользователя
user_data = {}

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_data[message.from_user.id] = {}
    await message.answer("Здравствуйте! Пожалуйста, введите ваш email.")

@dp.message_handler(lambda message: "@" in message.text)
async def email_handler(message: types.Message):
    user_id = message.from_user.id
    email = message.text.strip()

    if re.match(EMAIL_REGEX, email):
        user_data[user_id]["email"] = email
        await message.answer("Ваш email принят! Пожалуйста, введите текст сообщения.")
    else:
        await message.answer("Пожалуйста, введите корректный email.")

@dp.message_handler(lambda message: message.from_user.id in user_data and "email" in user_data[message.from_user.id])
async def text_handler(message: types.Message):
    user_id = message.from_user.id
    text = message.text.strip()
    email = user_data[user_id]["email"]

    # Отправка письма
    try:
        send_email(email, text)
        await message.answer("Ваше сообщение успешно отправлено!")
        del user_data[user_id]
    except Exception as e:
        await message.answer(f"Ошибка при отправке письма: {e}")

def send_email(to_email, message_text):
    # Создание MIME-сообщения
    msg = MIMEMultipart()
    msg["From"] = SMTP_EMAIL
    msg["To"] = to_email
    msg["Subject"] = "Сообщение от Telegram-бота"

    # Добавление текста письма
    msg.attach(MIMEText(message_text, "plain"))

    # Установка безопасного соединения
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)