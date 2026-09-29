import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech and display it."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to the microphone and convert speech to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()

        except sr.UnknownValueError:
            speak("Sorry, I could not understand. Please repeat.")
            return ""

        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
            return ""

        except sr.RequestError:
            speak("Sorry, the speech recognition service is unavailable.")
            return ""


def main():
    speak("Hello! I am your Python voice assistant.")
    speak("You can ask me for the time, date, or a web search.")

    while True:
        command = listen()

        if not command:
            continue

        if "hello" in command or "hi" in command:
            speak("Hello! How can I help you?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak("Today's date is " + current_date)

        elif "search" in command:
            search_query = command.replace("search", "", 1).strip()

            if search_query:
                speak("Searching for " + search_query)
                webbrowser.open(
                    "https://www.google.com/search?q=" +
                    search_query.replace(" ", "+")
                )
            else:
                speak("Please tell me what you want to search for.")

        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye!")
            break

        else:
            speak("I don't know that command yet. You can ask for the time, date, or a web search.")


if __name__ == "__main__":
    main()
