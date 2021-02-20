import speech_recognition as sr
import pyttsx3 as tts
import os
from selenium import webdriver

r = sr.Recognizer()

eng = tts.init()
eng.setProperty('rate',140)
eng.setProperty('voice',"english-us")

query = "What are we doing today? Sir?"
def askAndGet(query):
    eng.say(query)
    eng.runAndWait()


    with sr.Microphone() as source:
        print("say")
        audio = r.listen(source,timeout=3,phrase_time_limit=3)

    try:
        reply = r.recognize_google(audio)
        return reply
    except sr.UnknownValueError:
        reply = r.recognize_sphinx(audio)
        return reply
    except sr.RequestError:
        error = "Sorry Sir, I couldn't process your reply if you said something."
        eng.say(error)
        eng.runAndWait()
    

#on starup
ans = askAndGet(query)
print(ans)
req = "likewise"
if req == "likewise":
    site = "http://likewiseonline.com/login.php"
    browser = webdriver.Chrome()
    browser.get(site)
    user = browser.find_element_by_id("tex")
    user.clear()
    user.send_keys("admin")
    passw = browser.find_element_by_id("passw")
    passw.clear()
    passw.send_keys("admin")
    submit = browser.find_element_by_id("button")
    submit.click()
    os.system("gnome-terminal -- sh -c 'ssh likewf1d@103.53.43.82;bash'")
    print("yes")
