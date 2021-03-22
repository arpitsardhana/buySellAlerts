#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import smtplib, ssl
port = 465
password = 'HelloWorld!'
context = ssl.create_default_context()
sender_address= 'buysellpython@gmail.com'
recipient_address= 'nehassingh1501@gmail.com'
message = """\
Subject: Hi there

This message is sent from Python."""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
 server.login(sender_address, password)
 server.sendmail(sender_address,recipient_address,message)
