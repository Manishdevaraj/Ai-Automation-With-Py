import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Print the available voices for reference
for voice in voices:
    print("ID:\n", voice.id, "Name:\n", voice.name, "Lang:\n", voice.languages)
