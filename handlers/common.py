import json

from telebot import TeleBot
from telebot.types import Message



def reg_common_handlers(bot: TeleBot):

    @bot.message_handler(commands=['start'])
    def main(message):
        message_dict = message.json
        debug_text = json.dumps(message_dict, indent=2, ensure_ascii=False)

        safe_text = f"<pre>{debug_text[:4000]}</pre>"
        
        bot.send_message(message.chat.id, safe_text, parse_mode='HTML')


    @bot.message_handler(commands=['help'])
    def help(message):
        bot.send_message(message.chat.id, '<b>Help info</b>', parse_mode='HTML')

        bot.send_message(message.chat.id, 'Нажми на команды, чтобы скопировать или выполнить')


        bot.send_message(message.chat.id, '`привет` - для вывода приветствия\n`id` - чтобы получить свой id\n/start - для вывода информации пользователя\n/help - помощь', parse_mode='Markdown')



    @bot.message_handler()
    def info(message):
        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
        elif message.text.lower() == 'id':
            bot.reply_to(message, f'ID: {message.from_user.id}')