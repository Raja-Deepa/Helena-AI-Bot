import pyttsx3
import speech_recognition as sr
import  datetime
import wikipedia
import webbrowser
import os 
import smtplib
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("Good Morning  Miss Deepa!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Miss Deepa!")
    else:
        speak("Good Evening Miss Deepa!")


    speak(" I am your personal assistant Helena. Please inform me of how I may be of assistance to you.")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
           # print(e)
            print("Could you please repeat that...")
            return "None"
        return query
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('r.deepa042003@gmail.com','wivx awpv dunt iqmi')
    server.sendmail('r.deepa042003@gmail.com', to, content)
    server.close()



if __name__=="__main__":
    #speak("Hello, I am your virtual assistant Helena. How may I help you?")
     wishMe()
     while True:
     #if 1:
         query =  takeCommand().lower()
         #logic for executing tasks based on query
         if 'wikipedia' in query:
             speak('Searching Wikipedia...')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2) # give summary from wikipedia in 2 sentences
             speak("According to Wikipedia")
             print(results)
             speak (results)

         elif 'open youtube' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://www.youtube.com")

         elif 'open google' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://www.google.com")

         elif 'open gmail' in query:
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://www.gmail.com")

         elif 'open spotify' in query:
           spotify_path = "C:\\Users\\Lenovo\\Downloads\\SpotifySetup.exe"
           if os.path.exists(spotify_path):
            subprocess.Popen([spotify_path])
           else:
            speak("Spotify application not found.")


         elif 'open haveloc' in query:
            try:
               webbrowser.open("https://app.haveloc.com/login")
               speak("Opening Haveloc application.")
            except Exception as e:
               speak("Failed to open Haveloc application.")
               print(e)


         elif 'open whatsapp' in query:
            whatsapp_path = "C:\\Users\\Lenovo\\Downloads\\WhatsApp Installer.exe %s"
            if os.path.exists(whatsapp_path):
             subprocess.Popen([whatsapp_path])
            else:
             speak("WhatsApp application not found. Opening WhatsApp Web instead.")
             chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
             webbrowser.get(chrome_path).open("https://web.whatsapp.com/")

         
         elif 'time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Deepa, the time is {strTime}")
         elif 'code' in query: 
               codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
               os.startfile(codePath)


         elif 'email to deepa' in query:
             try:
                 speak("What should I say?")
                 content = takeCommand()
                 to = "r.deepa042003@gmail.com"
                 sendEmail(to, content)
                 speak("Email has been sent! ")
             except Exception as e:
               print(e)
               speak("Sorry Deepa.I am not able to send you ")
         elif 'quit helena' in query:
             speak("Thank you for using me. Have a nice day.")
             print("Quit command recognized. Exiting...")
             quit()
            




