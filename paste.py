import hangul_to_english
import keyboard
import mouse
from pyautogui import position, click, move 
from time import sleep
level = int(input("Automation Level(between 1 and 3) : "))
if level==1:
    while True:
        a= input()
        splited = []
        hangul_to_english.result = []
        for i in range(len(a)):
            splited.append(a[i])
        mouse.wait(button='left', target_types=('down',))
        for i in splited:
            hangul_to_english.main(i)
        for j in hangul_to_english.result:
            keyboard.press_and_release(j)
            sleep(0.01)
if level==2:
    mouse.wait(button='right', target_types=('down',))
    prompt_position = position()
    print("Registered!")
    while True:
        a= input()
        click(prompt_position.x, prompt_position.y ,clicks=1, interval=0, button='left')
        splited = []
        hangul_to_english.result = []
        for i in range(len(a)):
            splited.append(a[i])
        for i in splited:
            hangul_to_english.main(i)
        for j in hangul_to_english.result:
            keyboard.press_and_release(j)
            sleep(0.01)
        keyboard.send('enter')
        



if level==3:
    pass


        