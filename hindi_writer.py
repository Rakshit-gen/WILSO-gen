import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    while 1==1:
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='hi-In')
            print('YOU SAID',query)
        except Exception as e:
            print('say that again')
            pass
