import speech_recognition as sr

listener = sr.Recognizer()

try:
    print("Listening....")
    with sr.Microphone() as source:
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)

except:
    print("say that again")        