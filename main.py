import pyttsx3
import pywhatkit
import speech_recognition as sr
import pyautogui
import random
import winshell
from urllib.request import urlopen
from ecapture import ecapture as ecap
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import wikipedia
import pyjokes
import datetime
import json
import os
import sys
import time
from screen_brightness_control import get_brightness
from JARVISUI import Ui_GUIASSISTANT





engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    
    speak("hii sir,please tell me how can i help you")

class MainThread(QThread):
   def __init__(self):
      super(MainThread,self).__init__()

   def run(self):
       self.JARVIS()

   def STT(self):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        speak("listening")
        audio=r.listen(source)
        
    try:
        print("recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

        
    except:
        print("say that again")
        speak("say that again")
        return"none"
    query = query.lower()
    return query
   

   def JARVIS(self):
       wish()
       while True:
           self.query = self.STT()
           if 'good bye' in self.query:
              sys.exit()
        
           elif"what do you want"in self.query:
              speak("i want you")

           elif"volume up" in self.query:
              pyautogui.press("volumeup")
              speak("volume has been increased")
    
           elif"volume mute" in self.query:
              pyautogui.press("volumemute")
              speak("volume has been muted")

           elif"take screenshot" in self.query:
              
              pyautogui.screenshot("'my_screenshot.png")
              pyautogui.screenshot(region=(0,0, 300, 400))
              
              speak("screenshot has been captured")

           elif"get brightness" in self.query:
              current_brightness = get_brightness()
              print("Current screen brightness is:", current_brightness)

           elif"open youtube" in self.query:
              
              print("opening youtube")
              speak("opening youtube")
              print("what should i search on youtube")
              speak("what should i search on youtube")
              a=()
              pywhatkit.playonyt(a)

           elif"open google" in self.query:
              print("opening gogle")
              speak("opening google")
              print("what should i search on google")
              speak("what should i search on google")
              a=()
              pywhatkit.search(a)

           elif"empty recycle bin" in self.query:
              winshell.recycle_bin().empty(confirm= False,show_progress= False,sound= True)
              speak("recycle bin empty")

           elif"open camera" in self.query or "take a selfie" in self.query:
              speak("opening camera")
              ecap.capture(0, "sachin camera", "img.jpg")
              speak("thanks for posing")

           elif "will you be my bestfriend" in self.query:   
              speak("I'm not sure about, may be you should give me some time")

           elif"roll the dice" in self.query:
              result = random.randint(1,6)
              print(result)
              speak(result)

           elif"toss a coin" in self.query:
              speak("tossing a coin")
              print("tossing a coin")
              list = random.choice(list)
              print(result)
              speak(result)

         #   elif "tell me the time":
         #      strTime = datetime.datetime.now().strftime("% H: % M: % S")
         #      speak(f"sir,the time is {strTime}")
           
           elif "how are you" in self.query:
              speak("i am fine")
              speak("how are you sir")
            
           elif"fine" in self.query or "good" in self.query:
              speak("its good to know that you are fine")

           elif"who made you" in self.query:
              speak("i have been created by sachin sir")

           elif"tell me a joke" in self.query:
              speak(pyjokes.get_jokes())
           

          




startExecution = MainThread()

# FROM_MAIN,_ = loadUiType(os.path.join(os.path.tirname(__file__),""))
 
class Main(QMainWindow):
   def __init__(self):
      
      super().__init__()
      self.ui = Ui_GUIASSISTANT()
      self.ui.setupUi(self)
      self.ui.pushButton.clicked.connect(self.startTask)
      self.ui.pushButton_2.clicked.connect(self.close)

   def startTask(self):
       self.ui.movie = QtGui.QMovie("../../Downloads/7LP8.gif")
       self.ui.label.setMovie(self.ui.movie)
       self.ui.movie.start()

       self.ui.movie = QtGui.QMovie("../../Downloads/SVKl.gif")
       self.ui.label_2.setMovie(self.ui.movie)
       self.ui.movie.start()

       timer = QTimer(self)
       timer.timeout.connect(self.showtime)
       timer.start(1000)
       startExecution.start()

   def showtime(self):
      current_time = QTime.currentTime()
      current_date = QDate.currentDate()
      label_time = current_time.toString('hh:mm:ss')
      label_date = current_date.toString(Qt.ISODate)
      
      self.ui.textBrowser.setText(label_date)
      self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())



      

    
  

