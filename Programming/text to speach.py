import pyttsx3


def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties before adding anything to say
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

    # Get details about the available voices
    voices = engine.getProperty('voices')

    # You can select different voices here
    engine.setProperty('voice', voices[0].id)  # Male voice
    # engine.setProperty('voice', voices[1].id)  # Female voice

    # Add the text to be spoken
    engine.say(text)

    # Run the speech engine
    engine.runAndWait()


if __name__ == "__main__":
    while True:
        # Prompt the user to enter text
        text = input("Please enter the text you want to convert to speech (or type 'exit' to quit): ")

        # Check if the user wants to exit
        if text.lower() == 'exit':
            print("Exiting the program.")
            break

        # Convert the input text to speech
        text_to_speech(text)
