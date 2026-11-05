import os

from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton



def reg_common_handlers(bot: TeleBot):

    @bot.message_handler(commands=['start'])
    def send_welcome(message: Message):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        btn_price = KeyboardButton("✂️ Прайс-лист")
        btn_contacts = KeyboardButton("📍 Контакты")

        markup.add(btn_price, btn_contacts)

        user_name = message.from_user.first_name if message.from_user else 'Друг'

        welcom_text = (f"Привет, {user_name}! 👋\n\n"
            "Добро пожаловать в мужскую парикмахерскую **'LeadCut'**! 💈\n"
            "Мы делаем классические и современные стрижки, оформляем бороды и бреем опасной бритвой.\n\n"
            "Выберите интересующий вас раздел в меню ниже 👇")

        photo_path = "./media/boroda.png"

        if os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo:
                bot.send_photo(
                    message.chat.id,
                    photo,
                    caption=welcom_text,
                    reply_markup=markup,
                    parse_mode="Markdown"
                )
        else:
            bot.send_message(
                message.chat.id,
                welcom_text + "\n\n*(Картинка не найдена)*",
                reply_markup=markup,
                parse_mode="Markdown"
            )


    @bot.message_handler(commands=['help'])
    def help(message):
        bot.send_message(message.chat.id, '<b>Help info</b>', parse_mode='HTML')

        bot.send_message(message.chat.id, 'Нажми на команды, чтобы скопировать или выполнить')


        bot.send_message(message.chat.id, '`привет` - для вывода приветствия\n`id` - чтобы получить свой id\n/start - для вывода информации пользователя\n/help - помощь', parse_mode='Markdown')



