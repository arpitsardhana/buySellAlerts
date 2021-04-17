FROM python:3
WORKDIR /buySellAlerts
#ENV apikey=$apikey
#ENV password=$password
ADD makeapicall.py .
ADD config.json .
ADD stocks .
ADD apiwithsched.py .
ADD tickr .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "apiwithsched.py" ]
