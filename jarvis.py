import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import sys
import time
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    time.sleep(0.1)

def wishme():
    print("wishme() is being called")
    hour = int(datetime.datetime.now().hour)
    if 0<= hour <12:
        speak("Good Morning")
    elif 12<=hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")   
    speak("I am zira mam How may i help you") 

def takeCommand(): 
    # it takes microphone input from user and returns string output
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Say that again please...")
        return "None"
    except sr.RequestError as e:
        print(f"Error with the speech recognition service:{e}")
        return"None"
    return query



             


if __name__ == "__main__":
    wishme()
    
    query = takeCommand().lower()
    
     
     #logic Foe executing task based on query 


    if 'wikipedia' in query:
        speak("Searching for it...")
        query = query.replace("wikipedia", "")
        try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for your query. Please be more specific.")
        except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any results for your query.")
        except Exception as e:
                speak("An error occurred while searching.")

    elif 'open youtube' in query:
         webbrowser.open("youtube.com")
    elif 'open google' in query:
         webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")
    elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is {strTime}")
    elif 'open chatgpt' in query:
         webbrowser.open("chatgpt.com")
    
                     

    elif'exit' in query or 'quit' in query or 'stop' in query:
        speak("Goodbye, ma'am!")
        sys.exit()

    else:  
         speak("I didn't understand")  
            





