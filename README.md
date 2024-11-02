# Robot Speaker

## Author: Anurag

Welcome to `Robot Speaker`, a Python-based Text-to-Speech (TTS) application that uses the pyttsx3 library to convert text input into spoken words. Robot Speaker allows users to input any text, which it will then speak aloud using your system's default voice engine. Say `bored` when you’re done, and the program will sign off with a friendly farewell message!

## Features:

**Real-time Text-to-Speech:** Input text and hear it spoken aloud instantly.

**Interactive Session:**  Engage with the program in a simple, interactive format.

**Friendly Sign-Off:** If you type "bored," Robot Speaker will bid you farewell and end the session.

## Prerequisites:

Python 3.x installed on your system.

`pyttsx3` Python library (for text-to-speech functionality).

## Installation:

### Clone the Repository:

    git clone https://github.com/username/robot-speaker.git
    cd robot-speaker

### Install Required Library:
    Install pyttsx3 if you haven't already:
    pip install pyttsx3

## Usage

### Run the Script:

    Start the program by running the following command in your terminal: python robot_speaker.py

### Enter Text to Speak:

    After starting, you’ll see a prompt: What you want me to speak:
    Type any text, and Robot Speaker will read it aloud.
    To end the session, type bored. Robot Speaker will bid you farewell, and the program will exit.

### Example Usage

    Welcome to Robot Speaker Created by Anurag
    What you want me to speak: Hello there!
    <Robot Speaker speaks: "Hello there!">

    What you want me to speak: I am a text-to-speech robot.
    <Robot Speaker speaks: "I am a text-to-speech robot.">

    What you want me to speak: bored
    <Robot Speaker speaks: "Bye Bye Friend, Hope you enjoyed my service!!">
    
## How It Works:

**Initialization:** The pyttsx3 library initializes a text-to-speech engine on startup.

**Input Loop:** The program continuously prompts the user for text input.

**Text-to-Speech Conversion:** Each input is sent to the say function, which queues it for speech, and runAndWait executes the speech.

**Exit Condition:** If the user types "bored," the program will say goodbye and end the loop.

## Customization:

**Voice and Speed:**  `pyttsx3` allows users to customize voice properties, such as speed and gender. Modify the code as follows to set these properties:

    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('voice', voices[0].id)  # Change index for different voices
  
## Dependencies:

`pyttsx3`: This is a Python text-to-speech library compatible with Windows, macOS, and Linux. Install it with pip install `pyttsx3`.

## Contributing:

Contributions, feedback, and suggestions are welcome! Feel free to submit a pull request or open an issue.

## License:

This project is open source and available under the MIT License. See the LICENSE file for more information.
