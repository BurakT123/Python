import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

api_key = "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"

lang = 'en'


openai.api_key = api_key

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""
            
            try:
                said = r.recognize_google(audio, language='en')
                print(said)

                if "Friday" in said:
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":said}])
                    text = completion.choices[0].message.connect
                    speech = gTTS(text=text,lang=lang,slow=False, tld="com.au")
                    speech.save("fridaywelcome1.mp3")
                    playsound.playsound("fridaywelcome1.mp3")
            except Exception:
                print("Say somethings")

        return said
    
    get_audio()