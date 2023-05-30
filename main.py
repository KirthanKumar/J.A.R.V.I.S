import openai
import pyttsx3  
import speech_recognition as sr  
import datetime
import wikipedia  
import webbrowser
import os
import smtplib
import random

from config import apiKey

from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! ")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon! ")

    elif hour >= 17 and hour < 19:
        speak("Good Evening! ")

    else:
        speak("Good Night! ")

    speak("I am your virtual assistant. Please tell me how may I help you")


def ai(prompt):
    openai.api_key = apiKey
    text="OpenAI response for prompt: {prompt} \n *****************************************\n\n"
    
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt=prompt,
        temparature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_panalty=0,
        presence_penalty=0
    )
    try:
        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
    except:
        print("An exception occured")
        
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    
    # with open(f"Openai/prompt- {random.randint(1, 9246822259)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

chatStr = ""
def chat(query): #code whispherer can be used to automatically generate code
    global chatStr
    print(chatStr)
    openai.api_key = apiKey
    chatStr += f"Harry: {query}\n Jarvis:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temparature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_panalty=0,
        presence_penalty=0
    )
    try:
        speak(response["choices"][0]["text"])
        chatStr += f'{response["choices"][0]["text"]}\n'
        return response["choices"][0]["text"]
    except:
        print("An exception occured")
        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Connection error")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif name := 'stack overflow' in query:
            c = webdriver.ChromeOptions()
            c.add_argument("--incognito")
            driver = webdriver.Chrome(
                executable_path="C:\chromedriver.exe", options=c)
            driver.implicitly_wait(0.5)
            driver.get("https://www.stackoverflow.com")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow")
            
        elif 'play music' in query:
            music_dir = 'music folder\\path'
            songs = os.listdir(music_dir)
            no_of_songs = len(songs)
            randomNumber = random.randint(0, no_of_songs)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[randomNumber]))

        elif "play video" in query:
            video_dir = 'D:\\FFOutput\\Screen Record'
            Videos = os.listdir(video_dir)
            no_of_videos = len(Videos)
            randomNumber = random.randint(0, no_of_videos)
            # print(Videos)
            os.startfile(os.path.join(video_dir, Videos[randomNumber]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\kirthan kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # this is target og application vs code taken form properties
            os.startfile(codePath)
            
        elif 'quit' in query:
            speak("ok quitting sir")
            exit()

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')
            
        elif "using artificial intelligence" in query.lower():
            ai(prompt=query)

        elif 'how are you' in query:
            setMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            ans_qus = random.choice(setMsgs)
            speak(ans_qus)
            speak(" How are you'")
            ans_from_user_how_are_you = takeCommand()
            if 'fine' in ans_from_user_how_are_you or 'happy' in ans_from_user_how_are_you or 'good' in ans_from_user_how_are_you:
                speak('Great')
            elif 'sad' in ans_from_user_how_are_you or 'not good' in ans_from_user_how_are_you:
                speak('Tell me how can i make you happy')
            else:
                speak("I can't understand. Please say that again !")

        elif "reset chat" in query.lower():
            chatStr = ""

        else:
            chat(query)
