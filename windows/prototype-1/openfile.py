import pyttsx3 
import speech_recognition as sr
import datetime
import time
import random
import os


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
 
          
