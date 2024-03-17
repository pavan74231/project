import speech_recognition as sr 

def audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio)
            return text
        except:
            return 'Error'
        
print(audio_to_text(r"C:\Users\SURYA S\210623\TraumaChat\ChatAssistance\test3.mp3"))