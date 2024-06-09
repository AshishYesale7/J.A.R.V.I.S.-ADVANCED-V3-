import time

import pyautogui as ui
from DLG import open_dld
import random

from NetHyTech_Pyttsx3_Speak import speak


def open(text):
    x = random.choice(open_dld)
    speak(x+""+text,2)
    time.sleep(0.5)
    ui.hotkey("win")
    time.sleep(0.2)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")

