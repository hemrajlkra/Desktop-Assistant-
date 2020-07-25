import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if (hour==0 and hour<12):
        speak("Good morning Sir.")
    elif(hour>=12 and hour<18):
       speak("Good afternoon Sir.")
    else:
        speak("Good evening Sir.")
    speak("I am Mr. Robot, how may I help you.")



def takecommand():
    '''takes the microphone input from user'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.energy_threshold = 300
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising......")
        query = r.recognize_google(audio, language='en-hi')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        speak("say that again please..")
        print("Say that again please..")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    f=open("...../assignment/try.txt","r")
    lines=f.readlines()
    email=lines[0]
    password=lines[1]
    server.login(email,password)
    server.sendmail(email,to,content)
    f.close()




if __name__ =='__main__':
    wishme( )
    if 1:
        query= takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Here are some results,According to wikipedia")
            print(results)
            speak(results)
        elif "Open youtube" in query:
            webbrowser.open("youtube.com")


        elif "Open Google" in query:
            webbrowser.open("google.com")
        elif "Open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "music" in query:
            music_dir='F:\\hindi songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif "open atom" in query:
            atomPath="...Local\\atom\\atom.exe"
            os.startfile(atomPath)

        elif "open edge" in query:
            edge="...\\Application\\msedge.exe"
            os.startfile(edge)
        elif "open zoom" in query:
            zoom="...Zoom\\bin\\Zoom.exe"
            os.startfile(zoom)

        elif "open python" in query:
            pycharm="...softwares\pycharm - community - 2019.1.3.exe"
            os.startfile(pycharm)
        
        elif "who are you" in query:
            speak(" Hello World I am Mr.Robot, Speed 1 terahertz, memory 1 zeta byte.")
        elif "what can you do" in query:
            speak("Anything what's in my range.")
        elif "tell me something I don't know" in query:
            speak("You are ignoring good guys")

        elif "send an email" in query:
            try:
                speak("what should I say?")
                content=takecommand()
                to=""
                sendEmail(to,content)
                speak("Email has been sent, tell them to check.")
            except Exception as e:
                print(e)
                speak("Sorry bro..., I tried but I couldn't..")

        else:
            speak("Couldn't recognise please speak it loud.")




