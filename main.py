from config import TOKEN

TELEGRAM_BOT_TOKEN = TOKEN
import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    webAppTest = types.WebAppInfo("https://5d88-85-143-106-69.ngrok-free.app")
    one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest)
    keyboard.add(one_butt)
    bot.send_message(message.chat.id, 'Привет, я бот для проверки телеграмм webapps!)', reply_markup=keyboard)


bot.infinity_polling()
