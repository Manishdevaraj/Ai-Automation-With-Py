import pyttsx3 
import speech_recognition as sr
import datetime
import time
import random
import os
import requests
import webbrowser
import wikipedia
import pywhatkit


engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...") 
      r.pause_threshold=5
      audio=r.listen(source,timeout=1,phrase_time_limit=5)

    try:
      print("Recognizing...") 
      query=r.recognize_google(audio,language='en-in') 
      print(query)
    #   speak(query)

    except:
      speak("please tell me sir again")  

    
    return query 

def play_yt():
   speak("what should i search on youtube sir")
   qn=takecommand()
   pywhatkit.playonyt(qn)

def wiki():
   speak("what should i search on wikipedia,sir")
   qn=takecommand().lower()
   result= wikipedia.summary(qn,sentences=58)
   print(result)
   speak("according to wikipedia"+result)
def searchongoogle():
   speak("what should i shearch on google sir")
   qn=takecommand().lower()
   webbrowser.open(f"https://www.google.com/search?q={qn}")

def ip_addr():
   speak("searching your ip address")
   print("Searching your ip ........")
   ip = requests.get("https://api.ipify.org").text
   print(ip)
   speak(f"your ip address is {ip}")
 
 
def wish():
   hour = datetime.datetime.now().hour
   tt = time.strftime("%I : %M  %p")
   print(tt)

   if hour<=12 and hour>=0:
      a="good morning sir it's now time is, "
      speak(a+tt)
   elif hour>12 and hour<=18:
      b="good afternoon sir it's now time is, "
      speak(b+tt)
   else:
       c="good evening sir it's now time is, "
       speak(c+tt)
       
      
   d="what can i do for you sir", "tell me the command to do sir","how can i help you sir"  
   speak(random.choices(d))  

def opengoole():
   speak("opening google chrome sir")
   path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"  
   os.startfile(path) 
   speak("succsesfully chrome browser is opened")   

def opennotepad():
    speak("opening note pad")
    path ="C:\\Windows.old\\windows\\notepad" 
    os.startfile(path) 
    speak("succsesfully notepad is opened")  
def openbrave():
    speak("opening brave browser")
    path ="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk" 
    os.startfile(path)
    speak("succsesfully brave browser is opened")     
if __name__=="__main__":
 wish()



 q=takecommand().lower()
 if "open google"in q:
    opengoole()
 elif "open google browser" in q:
    opengoole()
 elif "open chrome browser" in q:
    opengoole() 
 elif "open chrome" in q:
    opengoole()    

 elif "open brave"in q:
   openbrave()
 elif  "open brave browser" in q:
    openbrave();  
 elif "open notepad" in q:
   opennotepad()
 elif "my ip address" in q:
    ip_addr()
 elif "my ip " in q:
    ip_addr()  
 elif "tell me ip address" in q:
    ip_addr()
 elif "search" in q:
    searchongoogle()
 elif "search in google" in q:
    searchongoogle()
 elif "search on google" in q:
    searchongoogle()     
 elif "search on wikipedia" in q:
    wiki() 
 elif "video on youtube" in q:  
    play_yt()
 elif "youtube" in q:  
    play_yt() 
      
 
          
