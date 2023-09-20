import pyttsx3
import speech_recognition as sr
import language_tool_python as ltp
import datetime
import wikipedia
import webbrowser as wb
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetings():
    hour = int(datetime.datetime.now().hour)

    if hour >= 3 and hour < 12:
        speak("Good Morning, namastay!!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon, namastay!!!")
    else:
        speak("Good Evening, namastay!!!")

    speak("I am suhl·maan kahn, How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("\n", query)
    except Exception as e:
        print("Say that again please.")
        speak("Say that again please.")
        return 'None'
    return query


if __name__ == '__main__':
    greetings()

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia,")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            wb.get(chrome_path).open('youtube.com')
        elif 'open whatsapp' in query:
            wb.get(chrome_path).open("web.whatsapp.com")
        elif 'open gmail' in query:
            wb.get(chrome_path).open("mail.google.com")
        elif 'open google' in query:
            wb.get(chrome_path).open("www.google.com")
        elif 'open spotify' in query:
            wb.get(chrome_path).open("www.spotify.com")

        elif 'play harry potter part 1' in query:
            mov_dir = 'F:\\Movies\\Harry Potter And The Sorcerers Stone 2001 [ Bolly4u.trade ] Dual Audio BRip .mkv'
            os.startfile(mov_dir)
        elif 'play the dark knight' in query:
            mov_dir = 'F:\\Movies\\The Dark Knight 2008 Dual Audio 720P BluRay[dualdl.net].mkv'
            os.startfile(mov_dir)

        elif 'stop' in query:
            print("Have a nice day!")
            speak("Have a nice day!")
            exit()

        elif 'exit' in query:
            print("Have a nice day!")
            speak("Have a nice day!")
            exit()

        elif 'kam khatm' in query:
            print("Have a nice day!")
            speak("Have a nice day!")
            exit()
