import pyttsx3

try:
    engine = pyttsx3.init()
    engine.say('yo ho')
    engine.runAndWait()
except Exception as e:
    print(f"An error occurred: {e}")