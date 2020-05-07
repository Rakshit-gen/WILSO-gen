#importing some modules
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
from time import ctime
import smtplib
import speech_recognition as sr
import requests
#using pyttsx3 module
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('volume',0.9)
engine.setProperty('rate',130)
while 1==1:
    def speak(audio):     #now it will speak until the prog runs
        engine.say(audio)
        engine.runAndWait()
        pass
            

    def wishme():           #writing a function to wish me
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            speak('Good morning!')
        elif hour >= 13 and hour <= 18:
            speak('Good afternoon!')
        else:
            speak('Good evening!')
        if datetime.date.today() == datetime.date(2020, 1, 16):
            speak('Happy Birthday TO you!')
        speak('I am wilso,your assist in service,what can i do for you')
        print('how can i help you')

    def takeCommand():        #Major part of the ai to understand what we say
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold=2
            audio=r.listen(source)
        try:
            print('Recognizing...')
            query=r.recognize_google(audio,language='en-in')
            print('User said:',query)
        except Exception as e:        #testing exceptions to prevent stopping of program run
            print(e)
            print('say that again please')
            return 'NONE'
        return query
    if __name__=='__main__':
        wishme()
    while True:
        query=takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            if ctime()==30:
                print('maybe it is very tough to find or there may be a network issue')
            else:
                results = wikipedia.summary(query, sentences=2)
                print('According to wikipedia', query, results)
                speak('According to wikipedia')
                speak(results)
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
            speak('opening...')
        elif 'open github' in query:
            webbrowser.open('www.github.com')
            speak('opening')
        elif 'time' in query:
            print(datetime.datetime.now())
            speak(datetime.datetime.now())
        elif 'thanks' in query:
            print('as per being your assist my work is it to help you out in every task')
            speak('as per being your assist my work is it to help you out in every task')
        elif 'open whatsapp' in query:
            webbrowser.open('web.whatsapp.com')
        elif 'send email' in query:
            try:
                speak('what to send?')
                content=takeCommand()
                to='rakshityourEmail@gmail.com'
                sendemail(to,content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak('sorry my friend,I am not able to send this email at the moment')

        elif 'who created you' in query:
            print('I was created by Rakshit Sisodia Dated 5 May 2020 by Python language')
            speak('I was created by Rakshit Dated 5 May 2020 by Python language')

        elif 'how are you' in query:
            print('as being a artifitial intellegence,i am fine,what about you')
            speak('as being a machine artifitial intellegence,i am fine,what about you')
        elif 'I am fine' in query:
            print('that is nice to know')
            speak('that is nice to know')



        elif 'play music' in query:             #you may change the music_dir as per need to the folder where your files exist
            music_dir = 'D:\\vedio songs\\2019'
            songs = os.listdir(music_dir)
            print(songs)
            r = random.randint(0, 40)
            os.startfile(os.path.join(music_dir, songs[r]))
            print('Listening...')
            speak('nice song ha')
            #THANK YOU




        
