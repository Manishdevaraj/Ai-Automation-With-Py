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
import urllib.request
import sys
import openai



engine =pyttsx3.init()
# voices =engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voices',voices.id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...") 
    #   z="tell me a commad,sir","command me,sir","what to do sir"
    #   speak(random.choice(z))
      r.pause_threshold=1
      audio=r.listen(source,timeout=100,phrase_time_limit=100)

    try:
      print("Recognizing...") 
      query=r.recognize_google(audio,language='en-in') 
      print(query)
    #   speak(query)

    except:
      z="tell me a command again,sir","command me again,sir","order me,sir"
      # speak(random.choice(z))  
      query=takecommand()
       
    
    return query 


def sent_msg():
   speak("enter the number")
   no=input("Enter the number\n")
   speak("Tell me the message")
   msg=takecommand()
   speak("specify the time")
   hour=int(input("Enter the time \n"))
   speak("specify the minutes")
   minu=int(input("Enter the minutes\n"))
   speak("Processing...")
   print("Processing....")
   t="105","100","120","200"
   speak(f"In {random.choice(t)} Seconds WhatsApp will open and after 15 Seconds Message will be Delivered!")
   pywhatkit.sendwhatmsg(no,msg,hour,minu)
   speak("successfull message has been delevered!...")
   print("successfull message has been delevered!...")


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
   speak("what should i search on google,sir")
   qn=takecommand()
   webbrowser.open(f"https://www.google.com/search?q={qn}")
   speak("succesfully initiated on google")


def chatgpt():
   speak("what to i search on chat gpt,sir")
   qn=takecommand().lower()
   speak("Serching....")
   print("Serching....")
   openai.api_key = "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"

# Define function to search using Chat GPT
   
   response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=qn,
      max_tokens=400,
      n=1,
      stop=None,
      temperature=0.9,
    )
   t=response.choices[0].text.strip() 
   print(t)
   speak(t)

def ip_addr():
   speak("searching your ip address")
   print("Searching your ip ........")
   ip = requests.get("https://api.ipify.org").text
   print(ip)
   speak(f"your ip address is {ip}")


def internetconnection():
    speak("checking your internet connection...")
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        speak("connected")
        return True
    except:
        speak("not connected!")
        return False

     
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


def full_listening():
   q=takecommand().lower()

   if "open google"in q:
     searchongoogle() 
   elif "hey saira"in q:
         d="what can i do for you sir", "tell me the command to do sir","how can i help you,sir"  
         speak(random.choices(d)) 
   elif "saira"in q:
         d="what can i do for you sir", "tell me the command to do sir","how can i help you,sir"  
         speak(random.choices(d))         
   elif "google browser" in q:
            searchongoogle()  
   elif "google" in q:
            searchongoogle()        
   elif "open google browser" in q:
            searchongoogle() 
   elif "open chrome browser" in q:
            searchongoogle() 
   elif "open chrome" in q:
            searchongoogle()
   elif "chrome" in q:
            searchongoogle() 
   elif "browser" in q:
            searchongoogle()           
   elif "brave" in q:
            openbrave()   
   elif "open brave"in q:
        openbrave()
   elif "brave browser" in q:
            openbrave()      
   elif  "open brave browser" in q:
            openbrave()  
   elif "open notepad" in q:
        opennotepad()
   elif "notepad" in q:
        opennotepad()  
   elif "my ip address" in q:
            ip_addr()
   elif "ip" in q:
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
   elif "wikipedia" in q:
            wiki()  
   elif "open wikipedia" in q:
            wiki()      
   elif "video on youtube" in q:  
            play_yt()
   elif "play a video on youtube" in q:  
            play_yt()   
   elif "youtube" in q:  
            play_yt() 
   elif "next video" in q:  
            play_yt() 
   elif "another video" in q:  
            play_yt()                   
   elif "send message" in q:
            sent_msg()
   elif "message" in q:
            sent_msg()
   elif "send message" in q:
            sent_msg()      
   elif "send a message" in q:
            sent_msg()         
   elif "whatsup" in q:
            sent_msg()   
   elif "whatsapp" in q:
            sent_msg()  
   elif "open whatsapp" in q:
            sent_msg()
   elif "internet" in q:
         internetconnection() 
   elif "internet connection" in q:
         internetconnection() 
   elif "check internet connection" in q:
         internetconnection()  
   elif "check internet connections" in q:
         internetconnection()  
   elif "internet connections" in q:
         internetconnection() 
   elif "check wi-fi" in q:
         internetconnection()    
   elif "check wi-fies" in q:
         internetconnection()  
   elif "wi-fi" in q:
         internetconnection() 
   elif "wi-fies" in q:
         internetconnection()

   elif "just stop" in q:
         speak("all of my function has been stoped,sir....")
         print("I Have Stop My Function,Sir......")  
         sys.exit() 
   elif "stop" in q: 
         speak("all of my function has been stoped,sir....")
         print("I Have Stop My Function,Sir......")  
         sys.exit()    
   elif "just stop allfunction" in q:  
         speak("all of my function has been stoped,sir....")
         print("I Have Stop My Function,Sir......") 
         sys.exit()  
   elif "stop all offunction" in q:  
         speak("all of my function has been stoped,sir....")
         sys.exit()                 
#    elif "set new password" in q:
#          set_passwd()
#    elif "change new password" in q:
#          set_passwd() 
   elif "password" in q:
         show_passwd() 
   elif "show password" in q:
         show_passwd()            
   elif "chat gpt" in q:
         chatgpt()
   elif "chat" in q:
         chatgpt()      
   else:
         x="sorry,not authenticable command,sir ","sorry,not a default command,sir","sorry,try another command"
         y=random.choice(x)
         print(y)
         speak(y)
   full_listening()


# def set_passwd():
#   global l_passwd
#   l_passwd="hira"
#   q=takecommand().lower()
#   l_passwd=q

l_passwd="hira"
def show_passwd():
      speak("Your password is")
      speak(l_passwd)
      print("Your Passwd : "+l_passwd)
  
def lock_2_ai():
      wish()
      full_listening()

def lock_1_ai():
      lock=takecommand().lower()
      if l_passwd in lock:
       lock_2_ai()
      elif "stop" in lock:
            speak("all of my function has been stoped,sir....")
            sys.exit() 
      else:
            speak("your password is wrong")
            lock_1_ai() 


if __name__=="__main__":
 speak("your ai zaira is initiated....")
 print("Your AI Zaira Is Initiated...")
 speak("Voice recognition has been initiated....")
 print("Voice Recognition Has Been Initiated....")
 





# lock=takecommand().lower()
# if "hira" in lock:
#       lock_1_ai()
#  wish()
#  full_listening()
#  if "open google"in q:
#      searchongoogle() 
#  elif "google browser" in q:
#      searchongoogle()  
#  elif "google" in q:
#      searchongoogle()        
#  elif "open google browser" in q:
#      searchongoogle() 
#  elif "open chrome browser" in q:
#      searchongoogle() 
#  elif "open chrome" in q:
#     searchongoogle()
#  elif "chrome" in q:
#     searchongoogle()     
#  elif "brave" in q:
#      openbrave()   
#  elif "open brave"in q:
#    openbrave()
#  elif "brave browser" in q:
#      openbrave()      
#  elif  "open brave browser" in q:
#     openbrave()  
#  elif "open notepad" in q:
#    opennotepad()
#  elif "notepad" in q:
#    opennotepad()  
#  elif "my ip address" in q:
#     ip_addr()
#  elif "ip" in q:
#     ip_addr()   
#  elif "my ip " in q:
#     ip_addr()  
#  elif "tell me ip address" in q:
#     ip_addr()
#  elif "search" in q:
#     searchongoogle()
#  elif "search in google" in q:
#     searchongoogle()
#  elif "search on google" in q:
#     searchongoogle()     
#  elif "search on wikipedia" in q:
#     wiki() 
#  elif "wikipedia" in q:
#     wiki()  
#  elif "open wikipedia" in q:
#     wiki()      
#  elif "video on youtube" in q:  
#     play_yt()
#  elif "play a video on youtube" in q:  
#     play_yt()   
#  elif "youtube" in q:  
#     play_yt() 
#  elif "send message" in q:
#     sent_msg()
#  elif "message" in q:
#     sent_msg()
#  elif "send message" in q:
#     sent_msg()      
#  elif "send a message" in q:
#     sent_msg()         
#  elif "whatsup" in q:
#     sent_msg()   
#  elif "whatsapp" in q:
#     sent_msg()  
#  elif "open whatsapp" in q:
#     sent_msg()             
 
          
