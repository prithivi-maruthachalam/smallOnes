import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("say")
    audio = r.listen(source,timeout=3,phrase_time_limit=3)

#print()
try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("whoa")
