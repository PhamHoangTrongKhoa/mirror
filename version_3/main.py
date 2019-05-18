from speech import Speech,a
import json
import requests
from knowledge import Knowledge

class main():
    #def start():
    
    def decide_action():
        recognizer, audio = Speech.listen_for_audio()
        speech = Speech.google_speech_recognition(recognizer, audio)
        if speech is not None: 
            main.action(str)

    def action(self, str):
        print(str)
        if 'weather' in str:
            self.weather_action()
        elif 'turn' in str and 'light' in str:
            if 'on' in str:
                self.light_action("on")
            elif 'off' in str:
                self.light_action("off")

    def weather_action(self):
        weather_json = Knowledge.weather_knowledge()

    def light_action(sefl, str = "on"):
        if str == "on":
            print ("The light is truned on")
        elif str == "off":
            print ("The light is turned off")
#main.decide_action()







'''
data = {
    "president":{
        "name": "Khoa",
        "sex": "nam",
        "old": 20
    }
}
with open("data_file.json","w") as write_file:
    json.dump(data, write_file)

with open("data_file.json","r") as read_file:
    str = json.load(read_file)
print(str)
print(str['president']['name'])

'''

