import requests
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)
engine.setProperty("rate", 190)  # how fast the assistant will speak

# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    apidict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=cef5f19b23f84410b667dc98f6432040",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=cef5f19b23f84410b667dc98f6432040",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=cef5f19b23f84410b667dc98f6432040",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=cef5f19b23f84410b667dc98f6432040",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=cef5f19b23f84410b667dc98f6432040",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=cef5f19b23f84410b667dc98f6432040"
    }

    speak("Which field news do you want? [business], [health], [entertainment], [science], [sports], [technology]")
    field = input("Type the field of news that you want: ")

    url = next((value for key, value in apidict.items() if key.lower() in field.lower()), None)

    if url is None:
        print("URL not found")
        speak("Sorry, I couldn't find news for that category.")
        return

    print(url)
    speak("Here is the first news.")

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data["articles"]

        for article in articles:
            title = article["title"]
            print(title)
            speak(title)

            news_url = article["url"]
            print(f"For more info, visit: {news_url}")

            a = input("[Press 1 to continue] and [Press 2 to stop]")
            if str(a) == "2":
                break

        speak("That's all for now.")

    else:
        print("Failed to fetch news. Error:", response.status_code)
        speak("Sorry, I couldn't fetch the news at the moment.")

latestnews()
