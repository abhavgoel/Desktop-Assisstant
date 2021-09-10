import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser 
import os
import smtplib
import pywhatkit as kit



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id) //to check voices whether M or F
engine.setProperty('voice',voices[0].id)


def speak(audio):
    newVoiceRate = 175
    engine.setProperty('rate',newVoiceRate)
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<16:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")

    speak("What is it you desire today ?")

def takeOrders():
    #converts mic input to string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing....")
            query=r.recognize_google(audio,language='en-in')
            print(f"You said : {query}\n")
        except Exception as e:
            print("Can you please repeat...")
            return "Not recognized..."
        return query

def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('your email address', 'email password')
            server.sendmail('abhavpy@gmail.com', to, content)
            server.close()

def sendMsg(to,content,hour,minute):
    kit.sendwhatmsg(to,content,hour,minute)
    speak("message sent")


if __name__ =="__main__":
    greet()
    # while True:
    if 1:
        query=takeOrders().lower()
    #code for orders given
        if 'wikipedia' in query:
            speak("Searching the wikipedia")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("wikipedia says")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Opening youtube")
            urL='youtube.com'
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(urL)
        
        elif 'open chrome' in query:
            speak("Opening chrome")
            urL='google.com'
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(urL)

        
        ##need to add a directory....offline songs player
        # elif 'play songs' in query:
        #     songs_dir='#address'
        #     songs=os.listdir(songs_dir)
        #     print(songs)
        #     os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'open chrome' in query:
            chromepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)

        elif 'send a mail' in query:
            try:
                speak("Tell me the content of the mail. would you?")
                content = takeOrders()
                speak("whom should i send it to ")
                to = input()   
                sendEmail(to, content)
                speak("Your email has been successfully sent")
            except Exception as e:
                print(e)
                speak("sorry i cant send this mail. please check again")

        elif 'send whatsapp message' in query:
            try:
                speak("what shoud i say")
                content=takeOrders()
                speak("whom should i send it to")
                to=input()
                sendMsg(to,content,datetime.datetime.now().hour,datetime.datetime.now().minute+2)  #enter number using country code
            except Exception as e:
                print(e)
                speak("sorry i cant send this message. please check again")

        
        


        
        


