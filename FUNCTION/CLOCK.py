import datetime
from NetHyTech_Pyttsx3_Speak import *



def what_is_the_time():
    try:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}",2)

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        speak(error_message, 2)

