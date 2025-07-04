# pip install pyttsx3 :- this is  for voice

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional, you can adjust volume, rate, etc.)
# engine.setProperty('rate', 150)  # Speed of speech
# engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Say something
names = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K"];
for name in names:
    print(engine.say(f"shout out to {name}"));
    engine.runAndWait()
# engine.say("Hello! I am a voice module.")

