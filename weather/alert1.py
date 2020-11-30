# -*- coding: utf-8 -*-

from twilio.rest import Client
import time
from datetime import datetime
from pytz import timezone
from time import gmtime, strftime
import json
import urllib.request
import threading
import tkinter as tk

# put your own credentials here 
class alertk(object):
    def __init__(self,interval=300):
        self.interval=interval
        thread=threading.Thread(target=self.run,args=())
        thread.daemon=True
        thread.start()
    
        
    def sendSMS(self,body):
      ACCOUNT_SID = "AC94708c93fbb603334e292f22ae0b8b11"
      AUTH_TOKEN ="b5fdf2c79acfccf8410c1fe1ae87ef95" 
      client = Client(ACCOUNT_SID, AUTH_TOKEN)
      mes = client.messages.create(to="+919845970485", from_="+16513494102", body=body)
      print (mes)
    
    def run(self):
        while True:
            url='http://api.openweathermap.org/data/2.5/weather?q=Bangalore,India&appid=87a06fefe50f97477e3db4af6b348825'
            obj=urllib.request.urlopen(url).read().decode()
            data=json.loads(obj)
            url1='http://api.openweathermap.org/data/2.5/forecast?q=Bangalore,India&appid=87a06fefe50f97477e3db4af6b348825'
            obj1=urllib.request.urlopen(url1).read().decode()
            forec=json.loads(obj1)
            t = float(float(data['main']['temp']) - 272.15)
            fmt = "%d-%m-%Y, %H:%M:%S"
            now_time = datetime.now(timezone('Asia/Kolkata'))
            msg = 'Station: ' + data['name'] + ' ' + now_time.strftime(fmt) + ': Weather: ' + data['weather'][0]['description'] + ', Temp: ' + str(float(t)) + 'C'
            fmt = "%d"
            forec_date = '2020-11' + str(int(now_time.strftime(fmt)) + 1) +' 12:00:00'
            for x in forec['list']:
                if(str(forec_date) in str(x['dt_txt'])):
                    t = float(float(x['main']['temp']) - 272.15)
                    msg += ' and ' + x['dt_txt'] + ' Weather:' + x['weather'][0]['description'] + ', Temp: ' + str(float(t)) + ' °C'
            
            print (msg)
            print ('SMS ID: ',)
            self.sendSMS(msg)
            print ('------------------------------------------------------------------------')
            time.sleep(self.interval)
            tk.messagebox.showinfo("MESSAGE","Sent Successfully")


tr=alertk()

