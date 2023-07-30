
from background import keep_alive

import requests
import random
import telebot
from bs4 import BeautifulSoup as b
import time


URL = 'https://www.anekdot.ru/random/anekdot/'
API_KEY = '6574444268:AAGYjpBwlgUFbmvEVE_Ky-2DoxLLFu9llng'
CHANNEL_NAME = '@test_annn'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    an = soup.find_all('div',class_='text')
    return [c.text for c in an]
  
list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)
bot = telebot.TeleBot(API_KEY)
# while True:
#   @bot.message_handler(commands=['start'])
  
#   def hello(message):
#       bot.send_message(message.chat.id, 'good')
  
#       # Делаем паузу в один час
      
#   @bot.message_handler(commands=['a'])
#   def jokes(message):
#       bot.send_message(message.chat.id,list_of_jokes[0])
#       del list_of_jokes[0]
#   while True:
#    for jokesss in list_of_jokes:
#       bot.send_message(CHANNEL_NAME, list_of_jokes[0])
#       del list_of_jokes[0]
#       time.sleep(300)
#       break
#   continue

for jokesss in list_of_jokes:
  bot.send_message(CHANNEL_NAME, list_of_jokes[0])
  del list_of_jokes[0]
  keep_alive()#запускаем flask-сервер в отдельном потоке. Подробнее ниже...
  bot.polling(non_stop=True, interval=0) #запуск бота
  time.sleep(600)
  # break



