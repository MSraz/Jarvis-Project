import pyttsx3
import speech_recognition as sr 
import datetime as dt
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getproperty('voices')
#print(voices[1].id)
engine.setproperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)

def wishMe ():
    hour = int(dt.dt.now().hour)
    
    if hour >=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
            speak("Good afternoon")

    else:
        speak("good evening")


def take_command():
     # This function takes in the users speech input and gives speech output 

    r = sr.Recognizer()
    with sr.Microphone() as source:

        print('listening')
        r.pause_threshhold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, Language='en-in')
        print(f"user said :{query}\n")
        
    except Exception as e:
        print(e)
        print("Say that again please ...")   
        return "None" 

    return query       


if __name__ == "__main__":

    wishMe()
    while True:
        query = take_command().lower()

# Logic for executing tasks based on query
if 'wikipedia' in query:
    speak('Searching wikipedia...')
    query=query.replace("wikipedia","")
    result = wikipedia.summary(query, sentances = 2)
    speak("According to wikipedia")
    speak(results)