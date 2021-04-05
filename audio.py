import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[29].id)
engine.say('Buenos dias, con que puedo ayudar hoy?')
engine.save_to_file('Colombia es bella','saludo.wav')
engine.save_to_file('Buenos dias, con que puedo ayudar hoy?','ayuda.wav')
engine.save_to_file('Yo no existo. Soy una persona artificial creada por Sandra','noexisto.wav')
engine.setProperty('voice',voices[8].id)
engine.save_to_file('Yo no existo. Soy una persona artificial creada por Sandra','noexisto-hombre.wav')
engine.runAndWait()

listener = sr.Recognizer()

audio = sr.AudioFile('noexisto-hombre.wav')

try:
    with audio as source:
        data = listener.record(source, duration=3000)
        command= listener.recognize_google(data,language='es-ES',show_all=True)
        print(command)
except Exception as e:
    print(e)