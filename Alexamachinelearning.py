import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import time
import webbrowser
import subprocess
from algorithm_machine import *


#   voicerecogniger section
def wish():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speek.say("Good Morning Pankaj")
        print("Good Morning Pankaj")
    if hour>=12 and hour<18:
        speek.say("Good Afternoon Pankaj")
        print("Good Afternoon Pankaj")
    if hour>18 and hour<24:
        speek.say("Good Evening Pankaj")
        print("Good Evening Pankaj")


listener=sr.Recognizer()
speek=pyttsx3.init()
voices=speek.getProperty('voices')
speek.setProperty('voice', voices[0].id)
wish()
speek.say("  I am pankaj  ")
speek.say("your assistant")
speek.say("what i can help you")
speek.runAndWait()
#      TEXT RECOGNIGE SECTION
def feedback(text):
    speek.say(text)
    speek.runAndWait()
#     MICROPHONE LISTENING SECTION
def my_command():
    try:
        with sr.Microphone() as source:
            print(" Listening......")
            vioce= listener.listen(source)
            print(" Processing..........")
            command=listener.recognize_google(vioce)
            command=command.lower()

            # if 'pankaj' in command:
            #     command=command.replace('pankaj',' ')
                # print(command)


                # feedback(command):


    except sr.UnknownValueError:
        print(" I am Sorry please speek something")
        pass
    return command
# REMOTE SECTION

# def runf():
while True:
    command=my_command()
    if 'time' in command:
        current_time=datetime.datetime.now().strftime('%I:%M:%p')
        print(current_time)
        feedback(current_time)
    elif 'date' in command :
        today_date=datetime.date.today()
        print(today_date)
        feedback(today_date)
    elif 'how are you' in command:
        print('i am ok and my day is good')
        feedback('i am ok and')
        feedback('my day is good')
    elif 'single' in command:
        feedback(" no i am relationship with wifi")
    elif 'good' in command:
        feedback("i am already good ")
        feedback('because i made by pankaj')
    elif 'freind' in command:
        feedback("shivam is your freinds")
    elif 'food' in command:
        feedback("i am eating battery")
        feedback("because i am virtual")
    elif 'eating' in command:
        feedback(' no i am eating your mind')
    elif 'who made you' in command or 'who created you ' in command or 'admin' in command:
        feedback("i am made by pankaj kumar")
        feedback("pankaj kumar student of computer science and engineering ")
        feedback("he live in doharighat ")
        feedback('distict mau in uttarpradesh')
        feedback("his father name is mister deenanath")
        feedback('his mother name is mises malti devi')
    elif 'what can do' in command:
        print("I can play any song\nI search any thing in google\nI can talk you ")
        print("I can give information current date time")
        print("I make a joke")
    elif 'awesome' in command:
        print("nice day")
        feedback("nice day")
    elif 'ok' in command:
        print("you can try more try more")
        feedback("ok dost")
    elif 'stop' in command or 'nothing' in command or 'shutdown' in command:
        print("thanks\nNice to talk you")
        feedback("thanks")
        feedback("Nice to talk you")
        break
    elif 'jokes' in command:
        print(pyjokes.get_jokes())
        feedback(pyjokes.get_jokes())

#search any thing in google using pywhatkit code write here.....
    elif 'play' in command:
        song=command.replace('play','')
        print("Ok your"+song+'  is playing')
        feedback("Ok your" +song+"is playing")
        pywhatkit.playonyt(song)
        break
    elif 'search' in command:
        topic=command.replace('search','')
        print ("your searching is progress")
        feedback("your searching is progress")
        feedback("dont worry")
        pywhatkit.info(topic,2)
        feedback('done')
        feedback("you can read information above")
    elif 'weather' in command:
        temp=command.replace('weather','Weather')
        pywhatkit.search(temp)
        feedback(" weather is search in google")
        time.sleep(5)
        break
    elif 'meaning' in command:
        meaning=command.replace('searching','')
        print("your "+meaning+"\tis searching")
        feedback("your meaning in progress")
        feedback('smile')
        pywhatkit.search(meaning)
# to open any link code here using webbrowser module
    elif 'open youtube' in command:
        webbrowser.open_new_tab("https://www.youtube.com/")
        feedback("Ok youtube opening on google")
        break
    elif 'open google' in command:
        webbrowser.open_new_tab("https://www.google.com/")
        feedback("Ok Google is opening ")
        break
    elif 'open facebook' in command:
        webbrowser.open_new_tab("https://www.facebook.com/")
        feedback("Ok facebook is opening ")
        break
    elif 'open whatsapp' in command:
        webbrowser.open_new_tab("https://web.whatsapp.com/")
        feedback("Ok Google is opening ")
        break
    elif 'open gmail' in command:
        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
        feedback("Ok Gmail is opening ")
        break
    elif 'open hindi news' in command:
        webbrowser.open_new_tab("https://ndtv.in/")
        feedback("Ok hindi news  is opening ")
        break
    elif 'open english news' in command:
        webbrowser.open_new_tab("https://timesofindia.indiatimes.com/")
        feedback("Ok english news  is opening ")
        break
    elif 'open today cricket' in command or 'cricket' in command:
        webbrowser.open_new_tab("https://www.cricbuzz.com/")
        feedback("Ok cricket is openning")
        print("Ok cricket news fetching")
        break
    #open any app in pc use subprocess modele
    elif 'open notepad' in command or 'notepad' in command:
        feedback("Ok notepad openning")
        subprocess.Popen("C:\\Windows\\system32\\notepad.exe")
        break
    elif 'open calc' in command:
        feedback("Ok calculater is openning")
        subprocess.Popen("C:\\Windows\\System32\\calc.exe")
        break
    elif 'open code' in command:
        feedback("Ok codeblock is openninng")
        subprocess.Popen("C:\\Program Files (x86)\\CodeBlocks")
        break
    # all algorithm command write here
    elif 'factorial' in command:
        feedback("Ok input a number")
        n=int(input(print("Enter a number to calculate factorial")))
        feedback("here your answer")
        print(fact(n))



    else:
        print("sorry\nthis word not my command list\nplease say again")
        feedback("sorry")
        feedback("this word")
        feedback("not my command list")
        feedback("please say again")









