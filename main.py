import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# Wake up func
def listen_for_wake_word():
    while True:
        with sr.Microphone() as source:
            print("Waiting for wake word...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        try:
            wake = recognizer.recognize_google(audio).lower()
            print("You said:", wake)

            if "hey jarvis" in wake or "wake up daddy's home" in wake:
                speak("Welcome home sir. How can I assist you?")
                return
        
        except sr.UnknownValueError:
            pass

        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the speech service.")

if __name__ == "__main__":
    # Call wake-up function first
    listen_for_wake_word()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            command = command.lower()

            print("You said:", command)
            
            # Command to open sites
            if "open youtube" in command:
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube")

            elif "open google" in command:
                webbrowser.open("https://www.google.com")
                speak("Opening Google")

            elif "open github" in command:
                webbrowser.open("https://github.com")
                speak("Opening GitHub")

            elif "open linkedin" in command:
                webbrowser.open("https://www.linkedin.com")
                speak("Opening LinkedIn")

            elif "open chat g p t" in command or "open chatgpt" in command:
                webbrowser.open("https://chatgpt.com")
                speak("Opening ChatGPT")

            elif "open gmail" in command:
                webbrowser.open("https://mail.google.com")
                speak("Opening Gmail")

            elif "open whatsapp" in command:
                webbrowser.open("https://web.whatsapp.com")
                speak("Opening WhatsApp")
            
            elif "open spotify" in command:
                webbrowser.open("https://open.spotify.com")
                speak("Opening Spotify")

            elif "open amazon" in command:
                webbrowser.open("https://www.amazon.in")
                speak("Opening Amazon")
            
            # Command to ask time
            elif "time" in command:
                current_time = datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {current_time}")
           
            # Open apps on laptop
            elif "open notepad" in command:
                os.system("notepad")
                speak("Opening Notepad")

            elif "open calculator" in command:
                os.system("calc")
                speak("Opening Calculator")
            
            elif "open command prompt" in command:
                os.system("start cmd")
                speak("Opening Command Prompt")
          
            # Command to shutdown or restart computer
            elif "shutdown computer" in command:
                speak("Shutting down computer")
                os.system("shutdown /s /t 5")

            elif "restart computer" in command:
                speak("Restarting computer")
                os.system("shutdown /r /t 5")

            elif "cancel shutdown" in command:
                os.system("shutdown /a")
                speak("Shutdown cancelled")

            # Weather
            elif "weather" in command:
                webbrowser.open("https://www.google.com/search?q=weather")
                speak("Showing today's weather")

            # Exit command
            elif "exit" in command or "quit" in command:
                speak("Goodbye Sir!")
                break

            else:
                speak("Sorry, I didn't understand that.")

        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand the audio")

        except sr.RequestError:
            speak("Speech service is unavailable")