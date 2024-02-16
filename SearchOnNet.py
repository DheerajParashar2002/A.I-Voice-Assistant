import pyttsx3
import speech_recognition
import wikipedia
import pywhatkit
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[4].id)
# print(voices[4])
engine.setProperty("rate",190) # how much fast assistant will speak

#       speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 # gap of 1 sec after printing lisening
        r.energy_threshold = 300 #with how much energy we should speak
        audio = r.listen(source,0,4) # will wait for 4 second then move on to next function
    try:
        print("Understanding ...")
        query =r.recognize_google(audio,language='en-in')
        print(f"You said {query}\n")
    except Exception as e:
        print("Please say that again")
        return "None"
    return query

query = take_command().lower()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("google search","")
        query = query.replace("Search on google","")
        speak("This is what i found on google .. ")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("No Output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found on youtube")
        query = query.replace("Youtube search", "")
        query = query.replace("Search on Youtube", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done with the work")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching on wikipedia...")
        query = query.replace("Wikipedia search", "")
        query = query.replace("Search on Wikipedia", "")
        results = wikipedia.summary(query,sentences=2)
        print("According to wikipedia.. " + results)
        speak("According to wikipedia.. " + results)
