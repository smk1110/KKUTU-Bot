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
    del_list=list()
    imsi=list()
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
            if text=='':
                print("장문 다 씀")
                continue
            elif text in del_list:
                text=file.readline()
                history[a]+=1
            file.close()
        else: text=a
        if text=='reset':
            history=dict()
            continue
        elif text[:3]=='삭제 ':
            target=text[3:]
            starting_word = target[0]
            try:
                file = open("Text_files\\"+starting_word+".txt", 'r', encoding='utf-8')
            except FileNotFoundError:
                print("File not found.")
                continue
            read=file.readline()
            while not read == '':
                if target in read:
                    imsi.append(read)
                read=file.readline()
            for i in range(len(imsi)):
                print(str(i)+". "+imsi[i])
            number=int(input())
            try:
                del_list.append(imsi[number])
                print(imsi[number]+" was deleted.")
            except:
                print("Deletion canceled")
            imsi=list()
            file.close()
            continue
                
        click(prompt_position.x, prompt_position.y ,clicks=1, interval=0, button='left')
        for i in hangul.convert(text):
            keyboard.press_and_release(i)
            sleep(0.01)
        keyboard.send('enter')
