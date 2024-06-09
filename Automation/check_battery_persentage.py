import psutil

from NetHyTech_Pyttsx3_Speak import speak


def battey_persentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    speak(f"the device is running on {percent}% battery power",2)
    