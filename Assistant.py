#module for speach 
import pyttsx3
#Module for dateTime
import datetime
#module for speach
import speech_recognition as sr
#for wikipedia 
import wikipedia
import webbrowser
#to access programs in os 
import os
#play random songs 
import random
#get user id and password and api 
import UserCreds
#Module for sending mail
from smtplib import SMTP
import smtplib
#Python jokes 
import pyjokes
#for sending requests to api like wolframalpha
import requests
#for using inbuild functions 
import wolframalpha

#import speaking engine and using microsoft api for voices 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
#Set properties and check voices
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)
#used to change the voice of the assitant
Voiceflag = 1


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
        print(e)
        speak("Say that again please....or Check the Internet")
        return "None"
    return query

#To send mail
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login(UserCreds.Email_id,UserCreds.Password)
    server.sendmail(UserCreds.Email_id,to,content)
    server.close()

#To set reminder 
def saveReminder(content):
    if "remind me to" in content:
        content = content.replace("remind me to","")
    Reminder = open(r"Reminders.txt", "a+")
    Reminder.write(content)
    Reminder.close()

#To get reminders
def getReminders():
    Reminder = open(r"Reminders.txt", "r+")
    speak(Reminder.readlines)
    Reminder.close()


def MainClass():
    wishMe()
    #Path for opening chrome in browser
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    while True:
        query = takeCommand().lower()
        #For switching of Anchit
        if query == "goodbye brother":
            speak("GoodBye Bro")
            break
        #Introduce yourself
        if "who are you" in query or "introduce yourself" in query:
            speak("My name is Anchit. I am an Artificial Intelligence Assistant program.")
        #for searching wikipedia
        if "wikipedia" in query:
            try:
                speak("Searching wikipedia...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                speak(result)
            except:
                speak("Sorry nothing found on wikipedia")
        #Youtube open in chrome
        elif "open youtube" in query:
            speak("Opening Youtube")
            if "search stand up" in query:
                webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query=standup")
            else:
                webbrowser.get(chrome_path).open("youtube.com")
        elif "speak" in query:
            query = query.replace("speak","")
            speak(query)
        elif "open google" in query:
            webbrowser.get(chrome_path).open("google.com")
        elif "change voice" in query:
            randomVoice = Voiceflag;
            while randomVoice == Voiceflag:
                randomVoice = random.randint(0, len(voices)-1)
            engine.setProperty('voice', voices[randomVoice].id)
            wishMe()
            Voiceflag = randomVoice
        elif "original voice" in query:
            engine.setProperty('voice', voices[1].id)
            wishMe()
        elif "play punjabi music" in query:
            webbrowser.get(chrome_path).open(
                "https://wynk.in/music/package/punjabi-top-50/bb_1512370496100")
        elif "play music" in query:
            speak("Playing... music.....")
            music_dir = "C:\\Users\\Anirudh\\Desktop\\Anirudh\\DataScience\\Git Projects\\Personal Assitant\\Music playlist"
            songs = os.listdir(music_dir);
            randomSong = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[randomSong]))
        elif "play rock music" in query:
            webbrowser.get(chrome_path).open(
                "https://wynk.in/music/playlist/feel-good-classic-rock/bb_1522918663585")
        #Get time 
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        #reminder
        elif "set a reminder" in query:
            try:
                speak("What should I remind you ?")
                content = takeCommand()
                saveReminder(content)
                speak("Reminder saved")
            except Exception as e:
                speak("Sorry could not set reminder")
        elif "my reminders" in query:
            try:
                getReminders()
                speak("I guess that's all I had to remind you, bro")
            except Exception as e:
                speak("Sorry could not fetch reminders")

        elif "toss a coin" in query:
            coinResult = random.randint(0,1)
            if coinResult == 0 :
                speak("Its a Head!")
            else :
                speak("Its Tails!")
        #Email 
        elif 'email to devika' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "devikabhutani@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry was not able to send mail.")
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'calculate' in query:
            try:
                app_id = UserCreds.AppId_Wolf
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            except:
                speak("Sorry couldnt compute")
