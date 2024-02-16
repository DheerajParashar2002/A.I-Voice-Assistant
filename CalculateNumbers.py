import wolframalpha
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[4].id)
engine.setProperty("rate", 190)  # how fast the assistant will speak


# speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wolfRamAlpha(query):
    apikey = "QKUJY2-5429JL23G4"
    requester = wolframalpha.Client(apikey)

    try:
        requested = requester.query(query)
        answer = next(requested.results).text
        speak(answer)
    except:
        speak("The values are not clear")


def calculator(query):
    term = str(query)
    term = term.replace("Sunday", "")
    term = term.replace("multiply","*")
    term = term.replace("minus", "-")
    term = term.replace("plus", "+")
    term = term.replace("divide", "/")

    try:
        result = eval(term)
        speak(f"The result is {result}")
    except:
        speak("The value is not calculable")


# # Example usage:
# # For Wolfram Alpha query
# query = "What is the capital of France?"
# wolfRamAlpha(query)
#
# # For calculator query
# query = "Calculate five plus six"
# calculator(query)
