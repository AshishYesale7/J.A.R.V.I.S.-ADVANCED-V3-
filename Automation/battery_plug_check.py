import random
import psutil
from DLG import plug_out, plug_in
from NetHyTech_Pyttsx3_Speak import speak


def check_plugin_status():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged

    while True:
        battery = psutil.sensors_battery()

        if battery.power_plugged != previous_state:
            if battery.power_plugged:
              random_low = random.choice(plug_in)
              speak(random_low,2)
            else:
              random_low = random.choice(plug_out)
              speak(random_low,2)

            previous_state = battery.power_plugged

previous_state = None
plug_in1 = ["charger is plugged check conform", "battery is charging that means charger is plugged check completed"]
plug_out1 = ["Charger status unplugged", "battery is not charging that means charger is not plugged check completed"]
def check_plugin_status1():
    global previous_state  # Use the global variable

    battery = psutil.sensors_battery()

    if battery.power_plugged != previous_state:
        if battery.power_plugged:
            random_low = random.choice(plug_in1)
            speak(random_low,2)  # Assuming speak function is defined
        else:
            random_low = random.choice(plug_out1)
            speak(random_low,2)  # Assuming speak function is defined

        previous_state = battery.power_plugged