import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print(e)
        return None
    return command


def run_alexa():
    command = take_command()
    print(command)

    if command:
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'search' in command:
            search_query = command.replace('search', '')
            talk('Searching ' + search_query)
            webbrowser.open('https://www.google.com/search?q=' + search_query)
        elif command.startswith('tell me about'):
            person = command.replace('tell me about', '').strip()
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'bye' in command:
            talk('Goodbye!')
            exit()
        else:
            talk('Please say the command again.')


while True:
    run_alexa()
