#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
from dotenv import load_dotenv
load_dotenv()

import requests, smtplib, ssl, os

def send_email(stockandprice):
 port = 465
 password = os.environ.get('password')
 message = ' '.join(("Stock status \n \n", "following stocks are less than the current price \n", stockandprice))
 #print (message)
 context = ssl.create_default_context()
 sender_address= 'buysellpython@gmail.com'
 recipient_address= ['nehassingh1501@gmail.com','arpitsardhana2008@gmail.com']
 with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
  server.login(sender_address, password)
  server.sendmail(sender_address,recipient_address,message)




base_url="https://financialmodelingprep.com/api/v3/quote/"
f = open("stocks", 'r')
stock_file=f.read().replace('\n', ',')
APIKEY= os.environ.get('apikey')
url = base_url + stock_file + '?apikey=' + APIKEY
print (url)
response=requests.get(url)
#print (response)
#print (response.json())
stock_result = response.json()
result={}
for result_dict in stock_result :
 price50day = result_dict['priceAvg50']
 currentprice = result_dict['price']
 if currentprice < price50day :
  less_price = str(price50day - currentprice)
  result[result_dict['symbol']] = less_price 
print (result)
send_email (str(result))
