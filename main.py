from config import TOKEN
from telebot import types
import telebot

bot = telebot.TeleBot(TOKEN, parse_mode=None)


def webAppKeyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    webAppTest = types.WebAppInfo("https://telegram.mihailgok.ru")  # создаем webappinfo - формат хранения url
    one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest)  # создаем кнопку типа webapp
    keyboard.add(one_butt)

    return keyboard


bot.send_message(message.chat.id, 'Привет, я бот для проверки телеграмм webapps!)', reply_markup=webAppKeyboard())
