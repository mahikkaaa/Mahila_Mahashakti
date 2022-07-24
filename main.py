import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser as web

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source, phrase_time_limit=6, timeout=3600)
            command = "waiting"
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    mt="https://mahikaagrawal2020.wixsite.com/website"
    mh="https://mahikaagrawal2020.wixsite.com/website/blank-page"
    vv="https://mahikaagrawal2020.wixsite.com/website/blank-page-1"
    mp="https://mahikaagrawal2020.wixsite.com/website/blank-9"
    ss="https://mahikaagrawal2020.wixsite.com/website/news-and-tips-1"
    eg="https://mahikaagrawal2020.wixsite.com/website/news-and-tips"
    cu="https://mahikaagrawal2020.wixsite.com/website/contact"
    ju="https://forms.gle/S7aExMXtn9hog5Yn8"
    mf="https://forms.gle/adBrZs2yREbdRhc48"
    vvf="https://forms.gle/qk4uUgxycUxa26BFA"
    ar="https://mahikaagrawal2020.wixsite.com/website/audio-resources"

    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open maksat' in command:
        web.get(path).open(mt)
    elif 'open mahila maha shakti' in command:
        web.get(path).open(mt)
    elif 'go to homepage' in command:
        web.get(path).open(mt)
    elif 'open mental health' in command:
        web.get(path).open(mh)
    elif 'take me to mental health section' in command:
        web.get(path).open(mh)
    elif 'open viksit vyapar' in command:
        web.get(path).open(vv)
    elif 'open milaap' in command:
        web.get(path).open(mp)
    elif 'open skill sikho' in command:
        web.get(path).open(ss)
    elif 'open virtual library' in command:
        web.get(path).open(eg)
    elif 'open contact us' in command:
        web.get(path).open(cu)
    elif 'fill the join us form' in command:
        web.get(path).open(ju)
    elif 'fill the milaap form' in command:
        web.get(path).open(mf)
    elif 'fill the viksit vyapar form' in command:
        web.get(path).open(vvf)
    elif 'open audio resources' in command:
        web.get(path).open(ar)
    else:
        talk('Please say the command again.')


while True:
    try:
        run_alexa()
    except UnboundLocalError:
        print("No command detected! Alexa has stopped working ")
        break