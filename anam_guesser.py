import random
import speech_recognition as sr
r=sr.Recognizer()
while 1==1:
    passw=input('enter the anagram of password or letters used in it')
    with sr.Microphone() as source:
        audio=r.listen(source)
        query=r.recognize_google(audio,language='en-in')
        query=query.lower()
        try:
            print('User said',query)
        except Exception as e:
            print(e)
            pass
        for x in range(1,100000):
            l=list(passw)
            random.shuffle(l)
            passw=''.join(l)
            k=passw
            if passw in query:
                print('You said=',k,'I guessed in',x,'tries')
                break
            else:
                print(passw,'wrong attempt',x)
        
