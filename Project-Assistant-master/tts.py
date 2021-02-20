import pyttsx3 as tts

eng = tts.init()
eng.setProperty('rate',140)
eng.setProperty('voice',"english-us")
eng.say("Hello Sir. What wil we be working on?")
eng.runAndWait()

