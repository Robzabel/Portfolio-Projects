#! /usr/bin/env python3
import requests 
import json
import time 
import notify2
import dbus


def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'Confirmed Cases: {data["cases"]} \nDeaths: {data["deaths"]}\n Recovered: {data["recovered"]}'
    
    notify2.init('Covid-Check')
    n = notify2.Notification('Covid-19 Updates', text )
    n.show()

update()



