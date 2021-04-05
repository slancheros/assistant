import speech_recognition as sr
import pyttsx3
# import pyaudio as aud


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
        # audio = sr.AudioFile("saludo.wav")
        #with audio as  source:
        data = listener.record(source, duration=20)
        command = listener.recognize_google(data,language='es-ES',show_all=True)
        print(command)

except Exception as e:
    print(e)
