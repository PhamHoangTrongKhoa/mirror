import requests as req
import json
import datetime

class Knowledge:
    def __init__(self):
        return

    def time_knowledge(self):
        currentDT = datetime.datetime.now()
        time_json = {
            "date":{
                "year": currentDT.year,
                "month": currentDT.month,
                "day": currentDT.day,
                "hour": currentDT.hour,
                "minute": currentDT.minute,
                "second": currentDT.second
            }
        }
        print ("Current date and time : ")
        #print (now.strftime("%Y-%m-%d %H:%M:%S"))
        print (currentDT.strftime("%a, %d %b, %Y"))
        print (currentDT.strftime("%I:%M:%S %p"))
        str_time = currentDT.strftime("%I:%M:%S %p")

        location_json = self.location_knowledge()
        str_day = location_json['state_prov'] + currentDT.strftime(", %d %b")
        return time_json, str_time, str_day

    def weather_knowledge(self):
        location_json = self.location_knowledge()
        latitude = location_json['latitude']
        longitude = location_json['longitude']
        str="https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&lat="+latitude+"&lon="+longitude
        weather=req.get(str)
        weather_json = json.loads(weather.text)
        print (weather_json['main']['temp'])
        return weather_json  

    def location_knowledge(self):
        location=req.get("https://api.ipgeolocation.io/ipgeo?apiKey=28bf9038d7544bf08e24ecd59aa54edd") 
        location_json = json.loads(location.text)
        print(location_json['state_prov'],location_json['district'])
        return location_json
