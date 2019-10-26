import json
from difflib import get_close_matches
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        
        tts = gTTS(text="Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0], lang='en')
        tts.save("goo.mp3")
        os.system("mpg321 goo.mp3")
        playsound.playsound('goo.mp3', True)
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
           
            output=translate(text)
            return output
        except:
            print("Sorry could not recognize what you said")
    

output=speech()
if type(output) == list:
    for item in output:
        print(item)
        tts = gTTS(text=item, lang='en')
        tts.save("goog.mp3")
        os.system("mpg321 goog.mp3")
        playsound.playsound('goog.mp3', True)
else:
    print(output)
    tts = gTTS(text=output, lang='en')
    tts.save("goog.mp3")
    os.system("mpg321 goog.mp3")
    playsound.playsound('goog.mp3', True)
