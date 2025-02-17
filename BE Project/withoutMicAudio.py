import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set the voice to a female voice


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
        talk('Sorry, I did not understand that.')
    except sr.RequestError:
        talk('Sorry, my speech service is down.')
    except Exception as e:
        print(f"Error: {str(e)}")

    return command


def run_alexa():
    command = take_command()
    if not command:
        return

    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif command.startswith('tell me about'):
        person = command.replace('tell me about', '').strip()
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
    time.sleep(1)
