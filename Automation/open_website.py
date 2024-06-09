import difflib
import random
import webbrowser
from DLG import websites, open_dld, success_open, open_maybe, sorry_open
from NetHyTech_Pyttsx3_Speak import speak

def openweb(text):
    # Convert the input to lowercase for case-insensitive matching
    website_names = text.lower().split()
    counts = {}

    # Count the occurrences of each website
    for name in website_names:
        counts[name] = counts.get(name, 0) + 1

    # List to store the URLs of websites to be opened
    urls_to_open = []

    # Open each website using webbrowser
    for name, count in counts.items():
        if name in websites:
            random_dlg = random.choice(open_dld)
            urls_to_open.extend([websites[name]] * count)

    # Open all the collected URLs
    for url in urls_to_open:
        webbrowser.open(url)

    # Speak after opening all websites
    if urls_to_open:
        randonsuccess = random.choice(success_open)
        speak(randonsuccess,2)
    else:
        # If no websites were opened, speak sorry message
        randonsorry = random.choice(sorry_open)
        speak(randonsorry + " named " + text,2)

