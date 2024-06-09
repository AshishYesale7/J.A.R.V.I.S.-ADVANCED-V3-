import requests # pip install requests
from NetHyTech_Pyttsx3_Speak import speak


def is_online(url="http://www.google.com", timeout=5):
    try:
        # Try to make a GET request to the specified URL
        response = requests.get(url, timeout=timeout)
        # Check if the response status code is in the success range (200-299)
        return response.status_code >= 200 and response.status_code < 300
    except requests.ConnectionError:
        return False

# Example usage
def internet_status():
    if is_online():
        x = "YES SIR ! I AM READY AND ONLINE"
        speak(x,2)
    else:
        x = "HEY THERE SIR ! I AM FRIDAY , SORRY BUT JARVIS IS CURRENTLY NOT ONLINE"
        print(x)
