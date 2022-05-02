import speech_recognition as sr
import soundfile as sf
import os



def recognise(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text,language="ru_RU")
            #print('Converting audio transcripts into text ...')
            #print(text)
            return text
        except:
            #print('Sorry.. run again...')
            return "Sorry.. run again..."

#print(recognise("test.wav")) <-- Для проверки
