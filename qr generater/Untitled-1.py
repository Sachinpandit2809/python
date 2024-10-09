

import pyautogui
import time
time.sleep(0)
p='no'
while p=='no':
    p=str(pyautogui.confirm(text=" I have a love game for you will you want to play ",title="love_wish",buttons=['yes','no']))
    if p=='yes':
        p='yes'
        q='no'
        while q!='yes':
            q=str(pyautogui.confirm(text=" will you be my valentine ",title="love_wish",buttons=['yes','no']))
            if q =='yes':
                a=str(pyautogui.alert(text="I love you dear 😘😍💓😍😘🌹🌹🌹🌹💕",title="love_wish",button='thanks'))
                
            