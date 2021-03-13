import speech_recognition as sr
import pyttsx3
import datetime


listener = sr.Recognizer()
alexa = pyttsx3.init()

voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():

    try:
        with sr.Microphone() as source:
            print('Your device is listening, Please speak...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is: ' + time)
        talk('Current time is: ' + time)
    else:
        print('Did not get it. Can you please tell it again')
run_alexa()