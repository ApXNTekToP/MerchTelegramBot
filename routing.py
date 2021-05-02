import telebot
import keyboard_bot
import re

# Bot Connect
token_bot = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = telebot.TeleBot(token_bot)


# Routing
def routing_bot(message):
    message.text = message.text.replace(" ", "").lower()
    if re.findall(r'купить💣', message.text):
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Купить 💣'")
    elif re.findall(r'корзина🧺', message.text):
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Корзина 🧺'")
    elif re.findall(r'заказы📦', message.text):
        main_menu = keyboard_bot.show_button_orders()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Заказы 📦'",
                         reply_markup=main_menu)
    elif re.findall(r'новости📜', message.text):
        main_menu = keyboard_bot.show_button_news()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Новости 📜'",
                         reply_markup=main_menu)
    elif re.findall(r'настройки⚙', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Настройки ⚙'",
                         reply_markup=main_menu)
    elif re.findall(r'помощь🆘', message.text):
        main_menu = keyboard_bot.show_button_help()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Помощь 🆘'",
                         reply_markup=main_menu)
    elif re.findall(r'начало🏠', message.text):
        main_menu = keyboard_bot.show_button_main_menu()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Начало🏠'",
                         reply_markup=main_menu)
    elif re.findall(r'позвонить📞', message.text):
        main_menu = keyboard_bot.show_button_help()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Позвонить 📞'",
                         reply_markup=main_menu)
    elif re.findall(r'написать✉', message.text):
        main_menu = keyboard_bot.show_button_help()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Написать ✉'",
                         reply_markup=main_menu)
    elif re.findall(r'помощьнасайте📘', message.text):
        main_menu = keyboard_bot.show_button_help()
        bot.send_message(message.chat.id,
                         "Выбран пункт меню: 'Помощь на сайте 📘'",
                         reply_markup=main_menu)
    elif re.findall(r'назад⬅', message.text):
        main_menu = keyboard_bot.show_button_main_menu()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Назад ⬅'",
                         reply_markup=main_menu)
    elif re.findall(r'имя', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Имя'",
                         reply_markup=main_menu)
    elif re.findall(r'телефон', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Телефон'",
                         reply_markup=main_menu)
    elif re.findall(r'адрес', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Адрес'",
                         reply_markup=main_menu)
    elif re.findall(r'город', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Город'",
                         reply_markup=main_menu)
    elif re.findall(r'уведомления🔔', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id,
                         "Выбран пункт меню: 'Уведомления 🔔'",
                         reply_markup=main_menu)
    elif re.findall(r'ктоты?' or r'ктоты', message.text):
        main_menu = keyboard_bot.show_button_main_menu()
        bot.send_message(message.chat.id,
                         "Я чат-бот с функцией автопродажи "
                         "\nинформационных или физических товаров."
                         "\nМой создатель ApXNTekToP (@ApXNNTekToP)"
                         "\nvk: https://vk.com/apxntektopp"
                         "\ngithub: https://github.com/ApXNTekToP",
                         reply_markup=main_menu)
    elif re.findall(r'чемтызанимаешься?' or r'чемтызанимаешься', message.text):
        main_menu = keyboard_bot.show_button_main_menu()
        bot.send_message(message.chat.id,
                         "Испытываю ядерное оружие ☢",
                         reply_markup=main_menu)
    elif re.findall(r'кактебязовут?' or r'кактебязовут', message.text):
        main_menu = keyboard_bot.show_button_main_menu()
        bot.send_message(message.chat.id,
                         "У меня пока что нет имени",
                         reply_markup=main_menu)
    else:
        main_menu = keyboard_bot.show_button_main_menu()
        bot.send_message(message.chat.id, "Я чуть-чуть не понял тебя...",
                         reply_markup=main_menu)
