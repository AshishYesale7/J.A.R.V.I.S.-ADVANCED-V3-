from Automation.Another_Automation_in_youtube import *
from Automation.caption_in_video import *
from Automation.manual_search_in_youtube import *
from Automation.play_music_in_youtube import *
from Automation.play_pause_video_in_youtube import *
from Automation.search_in_youtube import *
from DLG import *
from NetHyTech_Pyttsx3_Speak import *
from os import getcwd

def clear_input_file():
    with open(f"{getcwd()}\\input.txt", "w") as input_file:
        input_file.truncate(0) 

def check_song_name():
  while True:
    with open(f"{getcwd()}\\input.txt", "r") as input_text:
        input_text = input_text.read().lower()  # Convert to lowercase for consistency
        if input_text:
            play_music_on_youtube(input_text)
            break
        else:
            pass

def youtube_cmd(text):
    if text in x :
        clear_input_file()
        a = random.choice(q)
        speak(a,2)
        time.sleep(1)
        check_song_name()

    elif text in x1 :
        stop()
    elif text in x2 :
        play()
    elif text == "increase volume":
        volume_up()

    elif text == "decrease volume":
        volume_down()

    elif text == "seek forward":
        seek_forward()

    elif text == "seek backward":
        seek_backward()

    elif text == "seek forward 10 seconds":
        seek_forward_10s()

    elif text == "seek backward 10 seconds":
        seek_backward_10s()

    elif text == "seek backward frame":
        seek_backward_frame()

    elif text == "seek forward frame":
        seek_forward_frame()

    elif text == "seek to beginning":
        seek_to_beginning()

    elif text == "seek to end":
        seek_to_end()

    elif text == "seek to previous chapter":
        seek_to_previous_chapter()

    elif text == "seek to next chapter":
        seek_to_next_chapter()

    elif text == "decrease playback speed":
        decrease_playback_speed()

    elif text == "increase playback speed":
        increase_playback_speed()

    elif text == "move to next video":
        move_to_next_video()

    elif text == "move to previous video":
        move_to_previous_video()

    elif text == "toggle subtitles":
        toggle_subtitles()

    elif text == "increase font size":
        increase_font_size()

    elif text == "decrease font size":
        decrease_font_size()

    elif text == "rotate text opacity":
        rotate_text_opacity()

    elif text == "rotate window opacity":
        rotate_window_opacity()

    elif text == "pan up":
        pan_up()

    elif text == "pan down":
        pan_down()

    elif text == "pan left":
        pan_left()

    elif text == "pan right":
        pan_right()

    elif text == "zoom in":
        zoom_in()

    elif text == "zoom out":
        zoom_out()

    elif text == "go to search box":
        go_to_search_box()

    elif text == "toggle play/pause":
        toggle_play_pause()

    elif text == "toggle mute/unmute":
        toggle_mute_unmute()

    elif text == "toggle full screen":
        toggle_full_screen()

    elif text == "toggle theater mode":
        toggle_theater_mode()

    elif text == "toggle miniplayer mode":
        toggle_miniplayer_mode()

    elif text == "exit full screen":
        exit_full_screen()

    elif text == "toggle party mode":
        toggle_party_mode()

    elif text == "navigate forward":
        navigate_forward()

    elif text == "navigate backward":
        navigate_backward()

    elif text.endswith("search in youtube") or text.startswith("search in youtube") or text.endswith("search on youtube") or text.startswith("search on youtube"):
        text = text.replace("search in youtube","")
        text = text.replace("search on youtube","")
        youtube_search(text)

    elif text.endswith("search in current youtube window") or text.endswith("search on current youtube window") or text.endswith("search current youtube window") or text.startswith("search"):
        text.replace("search in current youtube window","")
        text.replace("search on current youtube window","")
        text.replace("search current youtube window","")
        text.replace("search current youtube window","")
        search_manual(text)

    else:
        pass

