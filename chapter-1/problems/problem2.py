# import external module

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Hello, I am your text-to-speech assistant.")
engine.runAndWait()

# -----------------------------------

import pyttsx3
pyttsx3.speak("I will speak this text")