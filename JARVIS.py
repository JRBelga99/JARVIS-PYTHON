#Libraries
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3") #FIND A MPG321 SUBSTITUTE

def recordAudio():
    r = sr.Recognizer() #Records Audio
    with sr.Microphone() as source: #Sets Microphone as input source
        print("Say something fancy!") #Prompts User to Speak
        audio = r.listen(source) #Takes input from Microphone

    #speech recognition using Google Speech Recognition
    try:
        #Takes input from microphone and prints onto screen
        print("You said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand")
    except sr.RequestError as e:
        print("Unable to find results from Google Speech Recognition Service; {0}".format(e))
    data = r.recognize_google(audio)
    return data

def JARVIS(data):
    if "how are you" in data:
        speak("I am fine, thank you for asking")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        i = data.rfind("where is") + len("where is")
        location = data[i:]
        location.replace(" ", "+")
        #data = data.split(" ")
        #location = data[2]
        speak(" Give me a moment, I will soon show you where to find" + location)
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

#Initialization
time.sleep(2)
speak("Hello, what can I do for you?")
while 1:
    JARVIS(recordAudio())



#if r.recognize_google(audio) == "damn it" or:
#    print ("Please do not swear in a professional work environment")
#if r.recognize_google(audio) == "what time is it":
#    print(ctime())
