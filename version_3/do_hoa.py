import tkinter as tk
import socket
import requests as req
from random import randint
import json
import datetime
import time
from knowledge import Knowledge

class Display():
    def __init__(self):
        self.window = tk.Tk()

    def GUI(self):
        self.window.title("Welcome to LikeGeeks app")
        self.window.geometry('1280x720')
        self.window.configure(background='black')

    def display(self):
        self.window.mainloop()

    def display_time(self):
        clock=tk.Label(self.window, text='Clock',font=('Arial',30),fg='white',bg='black')
        clock.place(relx=0.1,rely=0.2,anchor="center")
        dayOfweek=tk.Label(self.window, text='Day of Week',font=('Arial',20),fg='white',bg='black')
        dayOfweek.place(relx=0.1,rely=0.05,anchor="center")

    def home_page(self):
        self.GUI()
        knowledge = Knowledge()
        '''Location and time for home'''
        time_json, str_time, str_day = knowledge.time_knowledge()
        clock=tk.Label(self.window, text=str_day ,font=('Arial',17),fg='white',bg='black')
        clock.place(relx=0.1,rely=0.1,anchor="center")
        clock=tk.Label(self.window, text=str_time ,font=('Arial',30),fg='white',bg='black')
        clock.place(relx=0.1,rely=0.05,anchor="center")

        '''weather for home'''
        weather_json = knowledge.weather_knowledge()
        temp = weather_json['main']['temp']
        print(temp)
        #temp = float(5/9)*(float(temp)-32 )
        temp = int(temp) - 273
        print(temp)
        self.display()

'''
d = Display()
d.GUI()
d.display_time()
d.display()
'''
d = Display()
d.home_page()
