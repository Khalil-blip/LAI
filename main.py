import telebot
import requests
import json

# Telegram Bot API Token
TOKEN ='6153820587:AAG04cxJ0vOa24dhxz9_ilVxV97ymIbNbBc'

# Etherscan API Key
API_KEY = 'UXK21DC853UCRHKRP4XXGHEGHEXY5JJ2WI'

# Create a bot instance
bot = telebot.TeleBot(TOKEN)
bot.delete_webhook()

# Handle the start command
@bot.message_handler(commands=['start'])
def greet(message):
  bot.reply_to(message, "L investigates contracts for B/S taxes, liquidity, MP, and whether it is a Hp or not.")
#Trend
@bot.message_handler(commands=['trend'])
def greet(message):
  bot.reply_to(message, '''π΅ PROMOTION SLOT  | π | π |  CHAIN | PROMO
 
π₯ FlokiGrow       | π | π | πΈBSC | π° 904
 
π₯ TruthGPT        | π | π | πΈBSC | π° 882
 
π₯ TruthGPT        | π | π | πΉETH | π° 861
 
4οΈβ£ Kenny           | π | π | πΉETH | π° 634
 
5οΈβ£ FlokiZilla      | π | π | πΈBSC | π° 588
 
6οΈβ£ KingFloki       | π | π | πΈBSC | π° 581
 
7οΈβ£ Meta Floki      | π | π | πΈBSC | π° 522
 
8οΈβ£ FlokiKing       | π | π | πΈBSC | π° 506
 
9οΈβ£ FatherFloki     | π | π | πΈBSC | π° 456
 
π TruthGPT        | π | π | πΉETH | π° 452''')
  #Etherscan
@bot.message_handler(commands=['eth'])
def start(message):
    # Fetch data from Etherscan
    url = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey={}'.format(API_KEY)
    r = requests.get(url)
    data = json.loads(r.content)
    # Send data to user
    bot.send_message(message.chat.id, 'Price:  | π | π |  {} \nMarket Cap   | π | π | : {}'.format(data['result']['ethusd'], data['result']))
#bTC
@bot.message_handler(commands=['btc'])
def start(message):
    # Fetch data from Etherscan
    url = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey={}'.format(API_KEY)
    r = requests.get(url)
    data = json.loads(r.content)
    # Send data to user
    bot.send_message(message.chat.id, 'π₯Price:  | π | π |  {} \nπ₯Market Cap   | π | π | : {}'.format(data['result']['ethusd'], data['result']))
  
# Run the bot
bot.polling()