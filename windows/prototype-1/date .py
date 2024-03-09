import pyttsx3 
import speech_recognition as sr
import datetime
import time
import random


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
      speak(query)

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


if __name__=="__main__":
 wish()
          
