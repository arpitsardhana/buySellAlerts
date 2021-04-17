#!/usr/local/bin/python3
from dotenv import load_dotenv
load_dotenv()

from contextlib import redirect_stdout

import requests, smtplib, ssl, os, time, datetime, json, sys
from datetime import datetime

with open('./config.json') as config:
  config_data = json.load(config)

def send_email(stockandprice):
 password = os.environ.get('password')
 message = ' '.join(("Stock status \n \n", "following stocks are less than the current price \n", stockandprice))
 context = ssl.create_default_context()
 with smtplib.SMTP_SSL("smtp.gmail.com", config_data['SMTP port'], context=context) as server:
  server.login(config_data['sender_address'], password)
  server.sendmail(config_data['sender_address'],config_data['recipient_address'],message)
 print("Email sent")

def day_now():
 return datetime.today().weekday()

def time_now():
 return datetime.strftime(datetime.now(),"%H:%M:%S")

def trigger_condition(stock_result):
 result={}
 for result_dict in range (len(stock_result)) :
   price50day = stock_result[result_dict]['priceAvg50']
   currentprice = stock_result[result_dict]['price']
   if currentprice < price50day :
    less_price = price50day - currentprice
    result[stock_result[result_dict]['symbol']] = str("{:.2f}".format(less_price))
 print (result)
 return result


def callapi():
 f = open("stocks", 'r')
 stock_file=f.read().replace('\n', ',')
 APIKEY= os.environ.get('apikey')
 url = config_data['base_url'] + stock_file + '?apikey=' + APIKEY
 print (url)
 if not (config_data['stockmarketclose'] > time_now() >= config_data['stockmarketopen']): 
  f = open('makeapicall.log','a+')
  print(datetime.now(),':','Stock market is not open yet', file=f)
# while (config_data['stockmarketclose'] > time_now() >= config_data['stockmarketopen']) and (5 > day_now() >=0):
 response=requests.get(url)
 stock_result = response.json()
 result = trigger_condition(stock_result)
 send_email (str(result))
 f = open('makeapicall.log','a+')
 print(datetime.now(),':',result, file=f)

if __name__ == "__main__":
    callapi()
 
