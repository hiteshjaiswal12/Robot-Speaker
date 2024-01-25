from gtts import gTTS
import os

print("Welcome to Robo Speaker Created by Hitesh Jaisal")

while True:
    text = input("Enter what you want me to speak (type 'stop' to exit): ")

    if text.lower() == "stop":
        print("Bye Bye Friends")
        break

    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")


