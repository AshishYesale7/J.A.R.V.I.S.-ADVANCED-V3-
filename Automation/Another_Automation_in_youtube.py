import pyautogui

def pan_up():
    pyautogui.press('w')

def pan_down():
    pyautogui.press('s')

def pan_left():
    pyautogui.press('a')

def pan_right():
    pyautogui.press('d')

def zoom_in():
    pyautogui.press('+')

def zoom_out():
    pyautogui.press('-')

def go_to_search_box():
    pyautogui.press('/')

def toggle_play_pause():
    pyautogui.press('k')

def toggle_mute_unmute():
    pyautogui.press('m')

def toggle_full_screen():
    pyautogui.press('f')

def toggle_theater_mode():
    pyautogui.press('t')

def toggle_miniplayer_mode():
    pyautogui.press('i')

def exit_full_screen():
    pyautogui.press('esc')

def toggle_party_mode():
    pyautogui.write('awesome')

# Navigation Controls
def navigate_forward():
    pyautogui.press('tab')

def navigate_backward():
    pyautogui.hotkey('shift', 'tab')