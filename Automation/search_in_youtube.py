import random
import time
import pyautogui as ui
import webbrowser
from DLG import yt_search, s1, s2
from NetHyTech_Pyttsx3_Speak import speak


def youtube_search(text):
    dlg = random.choice(yt_search)
    speak(dlg,2)
    webbrowser.open("https://www.youtube.com/")
    time.sleep(4)
    ui.press("/")
    ui.write(text)
    s12 = random.choice(s1)
    speak( s12,2 )
    time.sleep(0.5)
    ui.press("enter")
    s12 = random.choice(s2)
    speak(s12,2)

