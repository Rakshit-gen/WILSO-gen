import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    while 1==1:
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='hi-In')     #Say hindi words as clear as possible
            print('YOU SAID',query)                              #Here you will recive what you have said
        except Exception as e:
            print('say that again')                              #Just to cope up with exceptions
            pass
