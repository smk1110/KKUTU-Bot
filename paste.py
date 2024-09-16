import hangul
import keyboard
import mouse
from pyautogui import position, click
from time import sleep
level = int(input("Automation Level(between 1 and 3) : "))
if level==1:
    while True:
        a= input()
        mouse.wait(button='left', target_types=('down',))
        for i in hangul.convert(a):
            keyboard.press_and_release(i)
            sleep(0.01)

if level==2:
    mouse.wait(button='right', target_types=('down',))
    prompt_position = position()
    print("Registered!")
    while True:
        a= input()
        click(prompt_position.x, prompt_position.y ,clicks=1, interval=0, button='left')
        mouse.wait(button='left', target_types=('down',))
        for i in hangul.convert(a):
            keyboard.press_and_release(i)
            sleep(0.01)
        keyboard.send('enter')
if level==3:
    mouse.wait(button='right', target_types=('down',))
    prompt_position = position()
    print("Registered!")
    history=dict()
    while True:
        a= input()
        if hangul.is_hangul(a):
            try:
                file = open("Text_files\\"+a+".txt", 'r', encoding='utf-8')
                try:
                    history[a]+=1
                except KeyError:
                    history[a]=1
            except FileNotFoundError:
                print("File not found.")
                continue
            for i in range(history[a]):
                text=file.readline()
            file.close()
        else: text=a
        if text=='reset':
            history=dict()
            continue
        click(prompt_position.x, prompt_position.y ,clicks=1, interval=0, button='left')
        for i in hangul.convert(text):
            keyboard.press_and_release(i)
            sleep(0.01)
        keyboard.send('enter')
        


        
