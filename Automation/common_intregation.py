from Automation.close import *


def common_cmd(text):
    if "close" in text or "band kar do" in text:
        close()
    else:
        pass