
import imp
import os
import pywhatkit
import wikipedia
import speech_recognition as sr
from pywikihow import search_wikihow
import pyttsx3
import webbrowser
from logging.config import listen, stopListening

print("Hello sir! I am your virtual assistant. How can i help you?")

engine = pyttsx3.init()
engine.say('Hello sir. I am your virtual assistant. How can i help you.')
engine.runAndWait()


print("Listening... Please give command !")
print("speak something :)")



r = sr.Recognizer()
with sr.Microphone(device_index=2) as source:
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print("You said : {}".format(text))
except:
    print("Sorry could not recognize what you said")
        
        
if text.lower() == "open google":
            webbrowser.open("google.com")
            engine = pyttsx3.init()
            engine.say('opening google.')
            engine.runAndWait()
            print("opening google...please wait")

elif text.lower() == "how are you":
            engine = pyttsx3.init()
            engine.say('I am fine sir  . and you?')
            engine.runAndWait()
            print('I am fine . and you')


elif text.lower() == "dhruv rathee youtube":
            webbrowser.open("https://www.youtube.com/c/dhruvrathee")
            print("opening youtube")

elif text.lower() == "open youtube":
            webbrowser.open("youtube.com")
            print("opening youtube...")

elif text.lower() == "mail radhey":
            webbrowser.open("https://mail.google.com/mail/u/1/#search/radhey2629gmail.com?compose=new")
            engine = pyttsx3.init()
            engine.say('it seems like radhey is your  friend.  opening gamil...')
            engine.runAndWait()
            print("opening google...please wait")


elif text.lower() == "play hanuman chalisa":
            webbrowser.open("https://www.youtube.com/watch?v=AETFvQonfV8")
            engine = pyttsx3.init()
            engine.say('it seems like you are spritual. opening youtube')
            engine.runAndWait()
            print("opening youtube...please wait")

            print("playing hanuman chalisa")

elif text.lower() == "mail anubhi":
            webbrowser.open("https://mail.google.com/mail/u/0/#search/anubhi25s%40gmail.com?compose=new")
            print("opening gmail")
 
elif text.lower() == "open whatsapp":
            webbrowser.open("https://webbrowser.whatsapp.com/")
            engine = pyttsx3.init()
            engine.say('opening whatsapp')
            engine.runAndWait()

            print("opening whatsapp...")

elif text.lower() == "i want to play games":
           webbrowser.open("https://poki.com/")
           print("opening poki...")
        
elif "weather" in text:
           webbrowser.open("https://www.google.com/search?q=current+weather&rlz=1C1VDKB_enIN998IN998&sxsrf=ALiCzsa7fxyy2agxTRoFOdGbxv4tVV5QcA%3A1657211773228&ei=fQvHYpzPDaDh4-EPub284AU&ved=0ahUKEwjcgb74muf4AhWg8DgGHbkeD1wQ4dUDCA4&oq=current+weather&gs_lcp=Cgdnd3Mtd2l6EAxKBAhBGABKBAhGGABQAFgAYABoAHAAeACAAQCIAQCSAQCYAQA&sclient=gws-wiz")

           print("opening weather page...")

elif text.lower() == "open vscode":
            codePathe = open("C:\\Users\\samradh joshi\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

elif text.lower() == "open facebok":
            webbrowser.open("https://www.facebook.com/confirmemail.php?next=https%3A%2F%2Fwww.facebook.com%2F")
            print("opening facebook...")

elif text.lower() == "my youtube":
            webbrowser.open("https://www.youtube.com/channel/UCBXt86YjqA4GvA_SPnEE8UA/featured")

elif text.lower() == "open instagram":

            webbrowser.open("https://www.instagram.com/")
            engine = pyttsx3.init()
            engine.say('opening instagram. login or signup first')
            engine.runAndWait()

            print("opening instagram")

#may not all comm will occur...

elif text.lower() == "arjeet singh songs":
           webbrowser.open("https://youtu.be/mbFwsbaX_L0")
           print("opening youtube music...")

elif text.lower() == "what is programming":
            webbrowser.open("https://www.freecodecamp.org/news/what-is-programming/")
            print("redirecting to the site...")

elif text.lower() == "open stack overflow":
            webbrowser.open("https://stackoverflow.com/")
            print("redirecting to the site...")

elif text.lower() == "linkedin":
            webbrowser.open("https://www.linkedin.com/feed/?trk=onboarding-landing")
            print(" opening linkedin")

elif text.lower() == "who is kejriwal":
            webbrowser.open("https://en.wikipedia.org/wiki/Arvind_Kejriwal")
            print("opening wikipedia")

elif text.lower() == "will you be my friend":
            engine = pyttsx3.init()
            engine.say('Offcourse sir, I am your friend since you created me!')
            engine.runAndWait()

elif "shahrukh Khan" in text:
            webbrowser.open("https://en.wikipedia.org/wiki/Shah_Rukh_Khan")
            print("redirecting to  shahrukhan's wikipedia")

elif text.lower() == "what is your name":
           engine = pyttsx3.init()
           engine.say('My name is jethalal. And one who created me is samradh joshi.')
           engine.runAndWait()


elif text.lower() == "what is your age":
           engine = pyttsx3.init()
           engine.say('my owner created me 3 weeks ago.')
           engine.runAndWait()
        


elif "Gaurav Taneja" in text.lower():
            print("according to google...")
            engine = pyttsx3.init()
            engine.say('according to google , Gaurav Taneja is currently one of the most popular YouTubers in the country with millions of subscribers across his three YouTube channels Flying Beast, Fit Muscle TV and Rasbhari Ke Papa where he makes fitness-related videos as well as his daily life vlogs and live streams.')
            engine.runAndWait()

elif "search" in text:
            text = text.replace("", "")
            text = text.replace("search", "")
            pywhatkit.search(text)
            engine = pyttsx3.init()
            engine.say('Thats what i found for your search! ')
            engine.runAndWait()
            print("Thats what i found for your search!")


elif "open zoom" in text:
            engine = pyttsx3.init()
            engine.say('opening zoom!. please wait for few seconds')
            engine.runAndWait()
            os.startfile( "C:\\Users\\samradh joshi\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
            print("opening zoom...")


elif "Chrome" in text:
            engine = pyttsx3.init()
            engine.say('opening google chrome!. please wait for few seconds')
            engine.runAndWait()
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            print("opening chrome...")


elif "Sam" in text:
            engine = pyttsx3.init()
            engine.say('yes sir? you call me?')
            engine.runAndWait()
            print("yes sir? you call me?")

elif "course" in text:
            engine = pyttsx3.init()
            engine.say('redirecting to the website. nice to hear that you are enrolled in python IT automation course!. ')
            engine.runAndWait()
            webbrowser.open("https://www.coursera.org/learn/python-crash-course/home/week/1")
            print("redirecting to the website. nice to hear that you are enrolled in python IT automation course!.")


elif "play music" in text:
            engine = pyttsx3.init()
            engine.say('playing music... please wait sir!  ')
            engine.runAndWait()
            os.startfile('C:\\Users\\samradh joshi\\Downloads\\Fast_Rap_Trap_Rap_Beat_Instrumental_(getmp3.pro).mp3')

elif 'Wikipedia' in text:
            print('Searching Wikipedia...')
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=2)
            engine = pyttsx3.init()
            engine.say('according to the wikipedia...')
            engine.runAndWait()
            engine = pyttsx3.init()
            engine.say(results)
            engine.runAndWait()
            
            
elif 'Youtube' in text:
            engine = pyttsx3.init()
            engine.say('opening youtube')
            engine.runAndWait()
            webbrowser.open("youtube.com")
    
      
            
else:
            engine = pyttsx3.init()
            engine.say('sorry, This function is not added yet....We will add this as soon as possible \nPlease give feedback and rate us')
            engine.runAndWait()
            print("sorry, This function is not added yet....We will add this as soon as possible \nPlease give feedback and rate us")



