import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot =  telebot.TeleBot('6354974513:AAEKGbGlAsogXNjdw0qBLBHUQ1D9roovHiY')

@bot.message_handler(commands=['start', 'hello'])
def start_message(message):
    bot.send_message(message.chat.id, "hello there!")

@bot.message_handler(commands=['update'])
def update_message(message):
    response = urlopen("https://kurs.onliner.by/")
    soup = BeautifulSoup(response)
    tags = soup.find_all('p', {'class':"value"})
    print(tags)
    buy = tags[0].text
    sell = tags[1].text
    euro_buy = tags[3].text
    euro_sell = tags[4].text

    bot.send_message(message.chat.id, "buy $ - " + buy + ", sell $ - " + sell)
    bot.send_message(message.chat.id, "buy € - " + euro_buy + ", sell € - " + euro_sell)

bot.polling()