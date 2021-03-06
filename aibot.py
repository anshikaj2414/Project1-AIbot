import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Bingo. How may I help you!")

def takeCommand():
    '''
    It takes microphone input from user and returns string output
    '''

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    if 1:
        query=takeCommand().lower()
        #logic for executing task
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open hacker rank' in query:
            webbrowser.open("hackerrank.com")
        

        elif 'play music' in query:
            music_dir='C:\\Users\\HP\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strTime}")
        elif 'open vscode' in query:
            vscodepath="C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodepath)
        







