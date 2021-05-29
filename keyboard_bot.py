from telebot import types


# Keyboards
def delete_keyboard():
    markup = types.ReplyKeyboardRemove()
    return markup


def show_button_register():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard="true")
    item_register = types.KeyboardButton(text="Зарегистрироваться ✏")
    markup.add(item_register)
    return markup


def skip():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard="true")
    item_skip = types.KeyboardButton(text="Пропустить шаг ✏")
    markup.add(item_skip)
    return markup


def show_button_main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard="true")
    item_buy = types.KeyboardButton(text="Купить 💣")
    item_basket = types.KeyboardButton(text="Корзина 🧺")
    item_orders = types.KeyboardButton(text="Заказы 📦")
    item_news = types.KeyboardButton(text="Новости 📜")
    item_settings = types.KeyboardButton(text="Настройки ⚙")
    item_help = types.KeyboardButton(text="Помощь 🆘")
    markup.add(item_buy, item_basket, item_orders,
               item_news, item_settings, item_help)
    return markup


def show_button_orders():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard="true")
    item_start = types.KeyboardButton(text="Начало 🏠")
    markup.add(item_start)
    return markup


def show_button_news():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard="true")
    item_start = types.KeyboardButton(text="Начало 🏠")
    markup.add(item_start)
    return markup


def show_button_settings():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard="true")
    item_name_settings = types.KeyboardButton(text="Имя")
    item_phone_settings = types.KeyboardButton(text="Телефон")
    item_adds_settings = types.KeyboardButton(text="Адрес")
    item_city_settings = types.KeyboardButton(text="Город")
    item_profile_settings = types.KeyboardButton(text="Мой профиль 👤")
    item_notice_settings = types.KeyboardButton(text="Уведомления 🔔")
    item_back_settings = types.KeyboardButton(text="Назад ⬅")
    markup.add(item_name_settings, item_phone_settings,
               item_adds_settings, item_city_settings, item_profile_settings) \
        .row(item_notice_settings) \
        .row(item_back_settings)
    return markup


def show_button_help():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard="true")
    item_call_help = types.KeyboardButton(text="Позвонить 📞")
    item_write_help = types.KeyboardButton(text="Написать ✉")
    item_website_help = types.KeyboardButton(text="Помощь на сайте 📘")
    item_back_help = types.KeyboardButton(text="Назад ⬅")
    markup.add(item_call_help, item_write_help,
               item_website_help).row(item_back_help)
    return markup


def show_button_update():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard="true")
    item_start_update = types.KeyboardButton(text="Начало 🏠")
    item_back_update = types.KeyboardButton(text="Назад ⬅")
    markup.add(item_start_update, item_back_update)
    return markup
