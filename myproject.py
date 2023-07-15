import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak("good morning my dudies , happy morning ! ")
    elif hour >= 12 and hour < 18 :
        speak("good afternoon my dudies,happy sunny day !")
    else :
        speak("good evening my dudies ! ")
    speak("let me tell how can i help you , what are you looking for ?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listing you supriya ...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("recognising your voice...")
        query = r.recognize_google(audio,language='en-in')
        print(f" my friend you said:{query}\n")


    except Exception as e:
        print("say that again please ....")
        return "none"
    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','')  #here you need to metion your email and password which you  use for emailing
    server.sendmail('abc@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()


        if 'open wikipedia ' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("accourding to wikipedia")
            print(results)
            speak(results)

        if 'open notepad' in query:
            npath ="C:\\windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open paint' in query:
            npath ="C:\\windows\\system32\\paint.exe"
            os.startfile(npath)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open chatgpt' in query:
            webbrowser.open('https://chat.openai.com/')

        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'tell me the time' in query:
            strTime = datetime.datetime.now("%H:%M:%S")
            speak(f"my dear frnd , the time is {strTime}")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        
        elif 'open whatsapp' in query :
            webbrowser.open("https://web.whatsapp.com/")

        elif 'github' in query:
            webbrowser.open("https://github.com/supriyaa2004")

        elif 'email to ansh' in query:
            try:
                speak("what should i send?")
                content =takecommand()
                to = "abcd@gmail.com"   #mention the mail id of those person whose you want to send the email
                sendEmail(to,content)
                speak("your email has been send")
            except Exception as e:
                print(e)
                speak("unable to send a email")
