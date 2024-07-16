import telebot
from src.config import TELEGRAM_BOT_TOKEN
from src.main import main

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to AI Biden Bot. Ask your questions.")

@bot.message_handler(func=lambda message: True)
def handle_question(message):
    question = message.text
    main(question)
    video = open('data/final_video.mp4', 'rb')
    bot.send_video(message.chat.id, video)

bot.polling()
