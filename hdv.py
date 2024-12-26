from gtts import gTTS
import os

# Function to speak the provided text
def speak(audio):
    tts = gTTS(text=audio, lang='en', slow=False)
    tts.save("speech.mp3")
    os.system("start speech.mp3")

# Test the speak function
speak("This is a test to check if TTS works.")

