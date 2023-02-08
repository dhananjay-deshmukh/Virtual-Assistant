import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices)



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
            if 'bosco' in command:
                command = command.replace('bosco', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()

   
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print('playing ' + song)
        pywhatkit.playonyt(song)
   
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        
        talk('Current time is ' + time)

   
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
   
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
   
    elif 'what is' in command:
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing,1)
        print(info)
        talk(info) 
   
    elif 'joke' in command:
        jokey = pyjokes.get_joke()
        print(jokey)
        talk(jokey)
    
    else:
        talk('Please say the command again.')


while True:
    run_alexa()