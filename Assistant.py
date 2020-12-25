#module for speach 
import pyttsx3
#Module for dateTime
import datetime
#module for speach
import speech_recognition as sr
#for wikipedia 
import wikipedia
import webbrowser

#import speaking engine and using microsoft api for voices 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
#Set properties and check voices
engine.setProperty('voice',voices[0].id)
#speach function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Function for intial program
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")
    elif hour >12 and hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("My name is Anchit ,How may I help you bro?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        #speak("User said:"+query)
        print(query)
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    #Path for opening chrome in browser
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    while True:
        query = takeCommand().lower()
        #For switching of Anchit
        if query == "goodbye brother":
            speak("GoodBye Sir")
            break
        #for searching wikipedia
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(result)
        #Youtube open in chrome
        elif "open youtube" in query:
    
            if "search stand up" in query:
                webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query=standup")
            else:
                webbrowser.get(chrome_path).open("youtube.com")
        elif "speak" in query:
            query = query.replace("speak","")
            speak(query)
        elif "open google" in query:
