from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
import sys
from bs4 import *
from requests import *
import schedule
import time




logging.basicConfig(level=logging.INFO,filename ='value.log',format = '%(asctime)s - %(levelname)s - %(message)s')
try:
    url = 'https://cbr.ru/currency_base/daily/'
    html = get(url).text
except:
    logging.critical('Сайт недоступен')
parsing = BeautifulSoup(html,'html.parser')
def usd():
    try:
        name_value = parsing.find('td',string = 'USD')
        value = parsing.find('td',string = 'Доллар США')
        return f'{name_value.text} = {value.find_next("td").text} Рублей'
        logging.info('Курс USD выдан')
    except Exception as e:
        logging.error('Курс USD не найден',e)
def euro():
    try:
        name_value = parsing.find('td', string = 'EUR')
        value = parsing.find('td',string = 'Евро')
        return f'{name_value.text} = {value.find_next("td").text} Рублей'
        logging.info('Курс EUR выдан')
    except Exception as e:
        logging.error('Курс EUR не найден',e)
def Sterling():
    try:
        name_value = parsing.find('td',string = 'GBP')ёёё
        value = parsing.find('td',string = 'Фунт стерлингов')
        return f'{name_value.text} = {value.find_next("td").text} Рублей'
        logging.info('Курс GBP выдан')
    except Exception as e:
        logging.error('Курс GBP не найден',e)
def yen():
    try:
        name_value = parsing.find('td',string = 'CNY')
        value = parsing.find('td',string = 'Юань')
        return f'{name_value.text} = {value.find_next("td").text} Рублей'   
        logging.info('Курс CNY выдан')
    except Exception as e:
        logging.error('Курс CNY не найден',e)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Я бот для вывода курса 4 валют к рублю, напишите /help чтобы увидеть команды')
TOKEN = ''

bot = ApplicationBuilder().token(TOKEN).build()
bot.add_handler(CommandHandler('start',start))
async def help(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Список команд: \
    /usd' \
    '/eur' \
    '/gbp' \
    '/cny')
async def usd_(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(usd())
async def eur_(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(euro())
async def gbp_(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(Sterling())
async def cny_(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(yen())
bot.add_handler(CommandHandler('help',help))
bot.add_handler(CommandHandler('usd',usd_))
bot.add_handler(CommandHandler('gbp',gbp_))
bot.add_handler(CommandHandler('cny',cny_))
bot.add_handler(CommandHandler('eur',eur_))
    
print('Бот запущен')
bot.run_polling()


