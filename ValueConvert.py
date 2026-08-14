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
        print(name_value.text,'=',value.find_next('td').text ,'Рублей')
        logging.info('Курс выдан')
    except Exception as e:
        logging.error('Курс не найден',e)
def euro():
    try:
        name_value = parsing.find('td', string = 'EUR')
        value = parsing.find('td',string = 'Евро')
        print(name_value.text,'=',value.find_next('td').text,'Рублей')
        logging.info('Курс выдан')
    except Exception as e:
        logging.error('Курс не найден',e)
def Sterling():
    try:
        name_value = parsing.find('td',string = 'GBP')
        value = parsing.find('td',string = 'Фунт стерлингов')
        print(name_value.text,'=',value.find_next('td').text,'Рублей')
        logging.info('Курс выдан')
    except Exception as e:
        logging.error('Курс не найден',e)
def yen():
    try:
        name_value = parsing.find('td',string = 'CNY')
        value = parsing.find('td',string = 'Юань')
        print(name_value.text,'=',value.find_next('td').text,'Рублей')
        logging.info('Курс выдан')
    except Exception as e:
        logging.error('Курс не найден',e)
print('Выберите команду чтобы увидеть курс(EUR,GBP,USD,CNY) или exit чтобы выйти')
while True:
    value = input().strip()
    if value.lower() == 'eur':
        euro()
    elif value.lower() == 'usd':
        usd()
    elif value.lower() == 'gbp':
        Sterling()
    elif value.lower() =='cny':
        yen()
    elif value.lower() == 'exit':
        logging.info('Программа закрыта')
        break

    else:
        print('Ошибка, пишите только доступную команду')



