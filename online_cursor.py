import time
import pyautogui
while True:
    pyautogui.moveRel(0,10)
    time.sleep(1)
    pyautogui.moveRel(0,-10)
    time.sleep(1)