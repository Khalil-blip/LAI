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
  bot.reply_to(message, '''🏵 PROMOTION SLOT  | 🔍 | 📈 |  CHAIN | PROMO
 
🥇 FlokiGrow       | 🔍 | 📈 | 🔸BSC | 🎰 904
 
🥈 TruthGPT        | 🔍 | 📈 | 🔸BSC | 🎰 882
 
🥉 TruthGPT        | 🔍 | 📈 | 🔹ETH | 🎰 861
 
4️⃣ Kenny           | 🔍 | 📈 | 🔹ETH | 🎰 634
 
5️⃣ FlokiZilla      | 🔍 | 📈 | 🔸BSC | 🎰 588
 
6️⃣ KingFloki       | 🔍 | 📈 | 🔸BSC | 🎰 581
 
7️⃣ Meta Floki      | 🔍 | 📈 | 🔸BSC | 🎰 522
 
8️⃣ FlokiKing       | 🔍 | 📈 | 🔸BSC | 🎰 506
 
9️⃣ FatherFloki     | 🔍 | 📈 | 🔸BSC | 🎰 456
 
🔟 TruthGPT        | 🔍 | 📈 | 🔹ETH | 🎰 452''')
  #Etherscan
@bot.message_handler(commands=['eth'])
def start(message):
    # Fetch data from Etherscan
    url = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey={}'.format(API_KEY)
    r = requests.get(url)
    data = json.loads(r.content)
    # Send data to user
    bot.send_message(message.chat.id, 'Price:  | 🔍 | 📈 |  {} \nMarket Cap   | 🔍 | 📈 | : {}'.format(data['result']['ethusd'], data['result']))
#bTC
@bot.message_handler(commands=['btc'])
def start(message):
    # Fetch data from Etherscan
    url = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey={}'.format(API_KEY)
    r = requests.get(url)
    data = json.loads(r.content)
    # Send data to user
    bot.send_message(message.chat.id, '🥇Price:  | 🔍 | 📈 |  {} \n🥇Market Cap   | 🔍 | 📈 | : {}'.format(data['result']['ethusd'], data['result']))
  
# Run the bot
bot.polling()