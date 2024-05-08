from multiprocessing.connection import Listener

import keyboard
import pyautogui
import pyttsx3  # pip install pyttsx3
import requests
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes  # pip install jokes
from bs4 import BeautifulSoup

Listener = sr.Recognizer()
engine = pyttsx3.init("sapi5")
rate = engine.getProperty('rate')
engine.setProperty('rate',int(rate * 0.75))
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("jarvis here at your service sir, How may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("could you please repeat it sir...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("21054cps053@gmail.com", "bangari2028")
    server.sendmail("21054cps053@gmail.com", to, content)
    server.close()


def temp():
    search="temperature in hyderabad"
    url=f"https://www.google.com/search?q={search}"
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temperature=data.find("div",class_="BNeawe").text
    speak(f"The temperature outside is {temperature}")

def screenshot():
    speak("okay")
    speak("what should i name the file")
    path = takeCommand()
    path1name = path + ".png"
    path1 = "D:\\" + path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    kk.startfile("D:\\")
    speak("screenshot is done")

def youtubeAuto():
    speak("youtube automation is started")
    while True:
        command = takeCommand()
        if "search" in command:
            query = query.replace("search", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
        elif "open" in command:
            keyboard.press('k')
        elif "forward" in command:
            keyboard.press('l')
        elif "backward" in command:
            keyboard.press('j')
        elif "exit youtube" or "close youtube" in command:
            break
def chromeAuto():
    speak("chrome automation is started")
    while True:
        command = takeCommand()
        if "close this tab" in command:
            keyboard.press_and_release("ctrl+w")
        elif "open new tab" in command:
            keyboard.press_and_release("ctrl+t")
        elif "open new window" in command:
            keyboard.press_and_release("ctrl+n")
        elif "chrome history" in command:
            keyboard.press_and_release("ctrl+h")
        elif "exit chrome" in command:
            break

if __name__ == "__main__":
    try:
        wishMe()
        while True:
            # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if "hello" in query:
                speak("hello madam")
                speak("I am jarvis")
                speak("I am your personal AI assistant")
                speak("how may i help you")
            elif "how are you" in query:
                speak("I am fine sir")
                speak("thank you for asking")
            elif "take a break" in query:
                speak("okay sir")
                speak("you can call anytime")
                break
            elif "bye" in query:
                speak("okay sir")
                speak("bye")
                break

            elif "website" in query:
                speak("okay sir")
                speak("this is what i found your search")
                query = query.replace("jarvis","")
                query = query.replace("website","")
                query = query.replace(" ","")
                web1 = query.replace("open","")
                web2 = "https://www."+web1+".com"
                webbrowser.open(web2)
                speak("launched")

            elif "wikipedia" in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif "open youtube" in query:
                webbrowser.open("youtube.com")
            elif "in youtube" in query:
                youtubeAuto()
            elif "in chrome" in query:
                speak("opening chrome browser")
                os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
                chromeAuto()
            elif "open google" in query:
                webbrowser.open("google.com")

            elif "open stackoverflow" in query:
                webbrowser.open("stackoverflow.com")

            elif "play music" in query:
                music_dir = "D:\\Non Critical\\songs\\Favorite Songs2"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif "send an email" in query:
                try:
                    speak("Enter the Recipient email address please")
                    email = input("Enter the Recipient email:")
                    speak("What should I say sir ?")
                    content = takeCommand()
                    to = email
                    sendEmail(to, content)
                    speak("Email has been sent sir!")
                except Exception as e:
                    print(e)
                    speak("Sorry boss. I am not able to send this email")

            elif "are you single" in query:
                speak("I am in a relationship with wifi")

            elif "joke" in query:
                speak(pyjokes.get_joke())
            elif "screenshot" in query:
                screenshot()
            elif "open chrome" in query:
                speak("opening chrome browser")
                os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            elif "open typing tutor" in query:
                os.startfile("C:\Program Files (x86)\TypingMaster10\ tmaster.exe")
            elif "open pycharm" in query:
                os.startfile("C:\Program Files\JetBrains\PyCharm Community Edition 2023.2.1\ bin\pycharm64.exe")
            elif "open facebook" in query:
                webbrowser.open("https://www.facebook.com/")
            elif "open instagram" in query:
                webbrowser.open("https://www.instagram.com/")
            elif "open google maps" in query:
                webbrowser.open("https://www.google.com/maps")
            elif "repeat my word" in query:
                while 1:
                    speak("tell me the word")
                    jj = takeCommand()
                    if "exit" in jj:
                        speak("ok i stopped repeating")
                        break
                    speak(f"you said {jj}")
            elif "set an alarm" in query:
                speak("enter the time please")
                time = input("Enter the time:")
                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")
                    if now == time:
                        speak("it's time to wake up")
                        speak("Alarm closed")
                    elif now > time:
                        break
            elif "remember that" in query:
                rememberMsg = query.replace("remember that","")
                rememberMsg = rememberMsg.replace("jarvis","")
                speak("you tell me to remind you that "+rememberMsg )
                remember = open("data.txt","w")
                remember.write(rememberMsg)
                remember.close()
            elif "what do you remember" in query:
                remember = open("data.txt","r")
                speak("you told me that "+remember.read())


        else:
            speak("Please say the command again sir.")
    except Exception as e:
        print(e)

