import os

from telebot import TeleBot
from telebot.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def reg_common_handlers(bot: TeleBot):

    @bot.message_handler(commands=["start"])
    def send_welcome(message: Message):
        markup = InlineKeyboardMarkup()

        btn_price = InlineKeyboardButton("✂️ Прайс-лист", callback_data="price")
        btn_contacts = InlineKeyboardButton("📍 Контакты", callback_data="contacts")
        btn_master = InlineKeyboardButton(
            "🧔‍♂️ Выбрать барбера", callback_data="master"
        )

        markup.row(btn_price, btn_contacts)
        markup.row(btn_master)

        user_name = message.from_user.first_name if message.from_user else "Друг"

        welcom_text = (
            f"Привет, {user_name}! 👋\n\n"
            "Добро пожаловать в мужскую парикмахерскую *'LeadCut'*! 💈\n"
            "Мы делаем классические и современные стрижки, оформляем бороды и бреем опасной бритвой.\n\n"
            "Выберите интересующий вас раздел в меню ниже 👇"
        )

        photo_path = "./media/boroda.png"

        if os.path.exists(photo_path):
            with open(photo_path, "rb") as photo:
                bot.send_photo(
                    message.chat.id,
                    photo,
                    caption=welcom_text,
                    reply_markup=markup,
                    parse_mode="Markdown",
                )
        else:
            bot.send_message(
                message.chat.id,
                welcom_text + "\n\n*(Картинка не найдена)*",
                reply_markup=markup,
                parse_mode="Markdown",
            )

    @bot.message_handler(commands=["help", "помощь", "FQ"])
    def help(message: Message):
        bot.send_message(
            message.chat.id,
            "📋 Доступные компанды:\n/start - Приветственное сообщение\n/help - Посмотреть команды\n/about - О нас",
        )

    @bot.message_handler(commands=["about", "о нас", "про нас"])
    def about(message: Message):
        bot.send_message(
            message.chat.id,
            "Добро пожаловать в *'LeadCut'* 💈 — закрытый мужской клуб, где чтят традиции классического бритья и парикмахерского искусства.\n\nМы создали пространство для мужчин, которые ценят свое время, безупречный внешний вид и высокий уровень сервиса.\nНаши барберы — дипломированные мастера, использующие премиальную мужскую косметику и проверенные временем техники.\n\nЗдесь вы можете замедлить ритм мегаполиса, расслабиться в удобном кожаном кресле и доверить свой стиль профессионалам.\nОткиньтесь назад, мы обо всем позаботимся.",
        )
