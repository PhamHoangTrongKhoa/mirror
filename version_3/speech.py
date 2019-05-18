import speech_recognition as sr

class Speech:  
    def listen_for_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        return r, audio

    def google_speech_recognition(r ,audio):
        try:
            str = r.recognize_google(audio)
            #print("You said: " + str)
            return str
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

'''def listen_for_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        str = r.recognize_google(audio)
        print("You said: " + str)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))'''

def a():
    print("happy")