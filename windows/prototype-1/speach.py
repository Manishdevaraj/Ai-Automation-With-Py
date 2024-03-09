import pyttsx3 
import speech_recognition as sr
from translate import Translator



engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices[1].id)
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

if __name__=="__main__":
 speak("tamil_translation")
 takecommand()
          
