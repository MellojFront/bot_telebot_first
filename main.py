import telebot
import os

from dotenv import load_dotenv
from handlers import common

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
if bot_token is None:
    raise ValueError("Ошибка: Переменная токена не найдена!")

bot = telebot.TeleBot(bot_token)

common.reg_common_handlers(bot)

if __name__ == '__main__':
    print("Bot starting...")
    bot.infinity_polling()