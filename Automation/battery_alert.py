import random
import time
import psutil
from DLG import low_b, last_low, full_battery
from NetHyTech_Pyttsx3_Speak import speak


def battery_alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            random_low = random.choice(low_b)
            speak(random_low,2)

        elif percent < 10:
            random_low = random.choice(last_low)
            speak(random_low,2)

        elif percent == 100:
            random_low = random.choice(full_battery)
            speak(random_low,2)
        else:
            pass

        time.sleep(1500)

def battery_alert1():
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            random_low = random.choice(low_b)
            speak(random_low,2)

        elif percent < 10:
            random_low = random.choice(last_low)
            speak(random_low,2)

        elif percent == 100:
            random_low = random.choice(full_battery)
            speak(random_low,2)
        else:
            speak("sir,your battery is in perfect battery level",2)

