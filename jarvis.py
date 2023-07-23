import pyttsx3                      # pip install pyttsx3
import speech_recognition as sr     # pip install speechRecognition # pip install pyaudio
import datetime
import wikipedia                    # pip install wikipedia
import webbrowser
import os
import smtplib
# import playsound

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice",voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hey, I am Jarvis, Please tell me how may I help you?")

def takeCommand():
    # It takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e) 
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("omgmore2005@gmail.com", "pass@2005")
    server.sendmail("omgmore2005@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    WishMe()
    # print(sr.Microphone.list_microphone_names())
    # print(sr.__version__)
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("youtube.com")

        elif "stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            webbrowser.open("youtube.com")

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is (strtime)")

        elif "open code" in query:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "email to me" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "omgmore2005@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send email at the moment")