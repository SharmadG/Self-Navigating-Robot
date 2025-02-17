import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info(person):
    try:
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Ambiguous search term. Please be more specific: {e.options}")
        talk("Ambiguous search term. Please be more specific.")
    except wikipedia.exceptions.PageError as e:
        print(f"Page not found. Please provide a valid search term: {e}")
        talk("Page not found. Please provide a valid search term.")
    except Exception as e:
        print(f"An error occurred: {e}")
        talk("An error occurred. Please try again.")

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        get_info(person)
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with WiFi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
