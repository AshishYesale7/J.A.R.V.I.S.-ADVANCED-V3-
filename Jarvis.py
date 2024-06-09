from NetHyTech_STT import listen
from brain import generate_response
import threading
from os import getcwd
from Automation._intregation_automation import Automation
from FUNCTION.function_intregation import Function_cmd
from NetHyTech_Pyttsx3_Speak import speak
import logging
import os

# Configure logging
log_file = os.path.join(os.getcwd(), "templates", "log.txt")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

bye_key_word = ["bye", "goodbye"]

# Variable to track if the bye command has been given
exit_flag = False

def clear_input_file():
    with open(f"{getcwd()}\\input.txt", "w") as input_file:
        input_file.truncate(0) 

def Check():
    global exit_flag
    output_text = ""
    while not exit_flag:
        try:
            with open("input.txt", "r") as input_text:
                current_text = input_text.read().lower()  # Convert to lowercase for consistency
            if current_text != output_text:
                output_text = current_text
                wake_cmd = output_text.strip()
                if "jarvis" in wake_cmd:  # Remove leading/trailing whitespaces
                    input_msg = f"User: {wake_cmd}"
                    reply = generate_response(wake_cmd)
                    output_msg = f"Jarvis: {reply}"
                    speak(reply, 2)
                    with open(os.path.join("templates", "log.txt"), "a") as log_file:
                        log_file.write(f"{input_msg}\n{output_msg}\n")
                else:
                    Automation(wake_cmd)
                    Function_cmd(wake_cmd)
                    with open(os.path.join("templates", "log.txt"), "a") as log_file:
                        log_file.write(f"User: {wake_cmd}\n")

                # Check if any of the bye keywords are in the wake command
                if any(keyword in wake_cmd for keyword in bye_key_word):
                    exit_flag = True
        except Exception as e:
            print("Error:", e)

def main():
    clear_input_file()
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=Check)
    t1.start()
    t2.start()
    t1.join()  
    t2.join()

