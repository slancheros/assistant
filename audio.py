import speech_recognition as sr
import pyttsx3




engine = pyttsx3.init()
voices = engine.getProperty('voices')
i=0
for v in voices:
    print(i)
    print(v)
    i= i+1


voice_female_spanish = voices[27].id
engine.setProperty('voice',voice_female_spanish)
engine.say('Надеюсь, вы узнали какие-то новые слова.')
# engine.save_to_file('Colombia es bella','saludo.wav')
# engine.save_to_file('Buenos dias, con que puedo ayudar hoy?','ayuda.wav')
# engine.save_to_file('Yo no existo. Soy una persona artificial creada por Sandra','noexisto.wav')
# engine.setProperty('voice',voices[8].id)
#engine.save_to_file('Yo no existo. Soy una persona artificial creada por Sandra','noexisto-hombre.wav')
engine.save_to_file('Надеюсь, вы узнали какие-то новые слова.','ruso.wav')
engine.runAndWait()

listener = sr.Recognizer()

audio = sr.AudioFile('ruso.wav')

try:
    with audio as source:
        data = listener.record(source, duration=3000)
        command= listener.recognize_google(data,language='ru-RU',show_all=True)
        print(command)
except Exception as e:
    print(e)