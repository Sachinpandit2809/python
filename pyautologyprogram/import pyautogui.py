import pyautogui
import time
time.sleep(0)
p='0'
while p=='0':
    p=pyautogui.confirm(text=" I have a love game for you will you want to play ",title="love_wish",buttons=['1','0'])
    if p=='1':
        p='1'
    # pyautogui.confirm(text=" will you be my valentine ",title="love_wish",buttons=["YES","NO"])