# Personal-Assistant
Python program to create personal assistant using speech recognition, Google API
and adding a simple UI using tkinter

run GUIBasics.py using python GUIBasics.py

Use requirement.txt to get all required packages (use pip install -r requirements.txt)

enable less secure apps in gmail to send mail(Store mail credentials in UserCreds.py and wolframalpha api details in the same file) 

# How to Install ?
Clone the project and install using pip install -r requirements.txt 

You can also create a virtual environment if you want by following :-

https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

(Make sure you dont use python3.7.6 as it doesnt work well with pyttsx3)

You can use virtualenv -p python3.7.5 [name_of_the_env] - to install virtual env command using a specific python version

or use conda create --name [name] python=3.7.5 - to install using conda 

Also create Contacts.csv containing columns : Name, Number,	Email Address in order to store your contacts for mail and whatsap and UserCreds.py with Email_id = "your_id@gmail.com",Password = "your_password" ,AppId_Wolf = "your_appId" variables for email credentials access and wolfralpha calculation api 

Create an account on Twilio and wolfralpha for getting authentication keys 

https://www.twilio.com/try-twilio

https://www.wolframalpha.com/



# Motivation 
To create a simple AI Assistant for small repititive tasks by using python libraries and some inbuild function and improving it with time and make use of neural networks. Fun-fact : I have named my AI bot Anchit(which is my real brother's name) cause he never works for me :P

# Functionality :-
1. Wikipedia 
2. Open google 
3. Play music 
4. Change voice 
5. Tell time 
6. send email (make sure to allow less secure apps for Gmail):
https://hotter.io/docs/email-accounts/secure-app-gmail/
7. Speak something 
8. Quit Functionality (goodbye brother)
9. Toss a coin
10. Tell a joke (using pyjokes api)
11. Calculate (using wolfmalpha api)
12. Simple UI (Using tkinter)


# To do :- 
1. Give good web interface , gtts import gTTS for text to speech 
2. read email
3. Search youtube 
5. News 
6. Dont listen 
7. Location 
8. Take a photo 
9. Reminder and ToDo list 
10. Weather 
11. Record songs 
12.  recognise user 
13. Random errors 
14. from pygame import mixer ( Background music ), random bye 
15. Add neural networks to automate responses instead of using simple if else to hard code 

# References 
https://medium.com/@singhpuneei/how-to-added-more-speakers-and-voices-in-pyttsx3-offline-text-to-speech-812c83d14c13

https://stackoverflow.com/questions/22445217/python-webbrowser-open-to-open-chrome-browser

https://www.youtube.com/watch?v=Lp9Ftuq2sVI&t=1577s

https://www.geeksforgeeks.org/voice-assistant-using-python/

https://dev.to/coderasha/build-virtual-assistant-with-python-automate-tasks-46a6

UI : https://dev.to/mshrish/making-a-simple-voice-controlled-personal-assistant-interface-using-python-5ce1

