import requests, smtplib, ssl, os, time, datetime, json, sys, flask
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, jsonify
from makeapicall import *

with open('./config.json') as config:
  config_data = json.load(config)
  
scheduler = BackgroundScheduler()

def get_tickr():
    APIKEY= os.environ.get('apikey')
    url = config_data['all_tickr_URL'] + '?apikey=' + APIKEY
    response = requests.get(url)
    result = response.json()
    open('tickr', 'w').close()
    for i in range (len(result)):
     f = open('tickr','a+')
     print(result[i]['symbol'], file=f) 
 
# scheduling the run of get_tickr function that propagates the tickrfile
#scheduler.add_job(get_tickr, 'interval', seconds = 50)
scheduler.add_job(get_tickr, 'cron', day_of_week='mon-fri',hour =1)

# scheduling the run of apicall function to get the latest ticker prices and send emails
#scheduler.add_job(callapi, 'interval', seconds = 50)
scheduler.add_job(callapi, 'cron', day_of_week='mon-fri',hour= '0-23')

scheduler.start()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    print(record['stock'])
    stock_val= record['stock']
    print (stock_val)
    with open('tickr') as tickrfile:
      if record['stock'] not in tickrfile.read():
       print ("tickr not valid")
       return("tickr not valid")
    with open('stocks') as myfile:
     if record['stock'] in myfile.read():
      print ("this tickr already exists in the stock list")
      return ("this tickr already exists in the stock list")
     else :
      f = open('stocks','a+')
      print(record['stock'], file=f)
      return ("ticker added")
     
#In debug mode, Flask's reloader will load the flask app twice and  causes apscheduler's jobs to be scheduled twice. Thus adding use_reloader=False
app.run(use_reloader=False, host="0.0.0.0")




