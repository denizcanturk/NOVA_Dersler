import pyautogui as p

import time
time.sleep(5)
text = """YOU FUCKING SCAMMERS...
YOU THING YOU CAN FOOL EVERYBODY"""
for i in range(150):
    p.typewrite(text)
    time.sleep(0.10)
    p.press("enter")
