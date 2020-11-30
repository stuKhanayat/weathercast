# -*- coding: utf-8 -*-
import tkinter as tk


from configparser import ConfigParser

import requests


url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file='config.ini'
config=ConfigParser()
config.read(config_file)
api_key=config['api_key']['key']




def get_weather(city):
        result=requests.get(url.format(city,api_key))
        if result:
            json=result.json()
            city=json['name']
            country=json['sys']['country']
            temp_kelvin=json['main']['temp']
            temp_celsius=temp_kelvin - 273.15
            temp_fahrenheit =(temp_kelvin - 273.15) * 9 / 5 + 32
            icon=json['weather'][0]['icon']
            weather= json['weather'][0]['main']
            final=(city,country,temp_celsius,temp_fahrenheit,icon,weather)
            return final
        else:
            return None



def search():
        city=city_text.get()
        weather=get_weather(city)
        if weather:
            
            location_lbl['text']= '{}, {}'.format(weather[0], weather[1])
            img['file']='C:/Users/Stuti/miniproject/weather_icons\\{}.png'.format(weather[4])
            temp_lbl['text']='{:.2f}°C, {:.2f}°F'.format(weather[2],weather[3])
            weather_lbl['text']= weather[5]
        else:
            tk.messagebox.showerror('ERROR','Cannot find city {}'.format(city))




root=tk.Tk()
root.title(" WEATHER APP")
root.geometry("700x350")



city_text = tk.StringVar()
city_entry=tk.Entry(root ,textvariable=city_text)
city_entry.pack()



search_btn=tk.Button(root,text='Search Weather',width=12,command=search)
search_btn.pack()

img=tk.PhotoImage(file='')
Image=tk.Label(root,image=img).pack()



location_lbl = tk.Label(root,text='',font=('bold,20'))
location_lbl.pack()


        

temp_lbl=tk.Label(root,text='')
temp_lbl.pack()

weather_lbl=tk.Label(root,text='')
weather_lbl.pack()








root.mainloop()
