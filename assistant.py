import speech_recognition as sr
#import pyaudio as aud
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[29].id)
engine.say('Buenos dias, con que puedo ayudar hoy?')
engine.runAndWait()
listener = sr.Recognizer()


try:
    with sr.Microphone(device_index=2) as source:
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
        print('listening...')

        listener.adjust_for_ambient_noise(source)
        data = listener.record(source, duration=20)

        audio = sr.AudioFile("saludo.wav")
        with audio as  source:
            command = listener.recognize_google(source,language='en-US',show_all=True)
        print(command)

except Exception as e:
    print(e)
