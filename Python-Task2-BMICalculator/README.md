# OIBSIP Python Internship – Task 1

## Voice Assistant

This project is developed as part of the Python Programming Internship at Oasis Infobyte.

## Objective

To build a Python-based voice assistant that listens to spoken commands and responds with useful actions.

## Features

- Captures voice input using a microphone.
- Responds to "Hello" with a predefined greeting.
- Tells the current time.
- Tells the current date.
- Performs a web search based on the user's spoken command.
- Provides text-to-speech feedback.
- Handles speech that is not understood.
- Allows the user to exit the assistant using a voice command.

## Technologies Used

- Python 3.12
- SpeechRecognition
- PyAudio
- pyttsx3
- datetime
- webbrowser

## How It Works

1. The program starts the voice assistant.
2. The assistant welcomes the user using text-to-speech.
3. The microphone captures the user's spoken command.
4. SpeechRecognition converts the voice input into text.
5. The program checks the command.
6. Based on the command, it tells the time/date or opens a web search.
7. The assistant provides a spoken response.
8. The user can say "exit", "quit", or "stop" to close the program.

## Example Commands

- "Hello"
- "What is the time?"
- "What is today's date?"
- "Search Python programming"
- "Exit"

## Testing

The voice assistant was tested successfully for:

- Greeting response
- Time response
- Date response
- Web search
- Voice recognition
- Text-to-speech response
- Exit command

## Outcome

Successfully developed and tested a beginner-level Python voice assistant capable of recognizing spoken commands and performing basic useful actions.

## Internship

Oasis Infobyte – Python Programming Internship

Task 1: Voice Assistant