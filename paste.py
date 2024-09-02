import hangul_to_english
import keyboard
import wait_for_click
import time
while True:
    key = keyboard.read_key()
    if key == 'esc': exit()
    a=input()
    splited = []
    hangul_to_english.result = []
    for i in range(len(a)):
        splited.append(a[i])
    wait_for_click.main()
    for i in splited:
        hangul_to_english.main(i)
    for j in hangul_to_english.result:
        keyboard.press_and_release(j)
        time.sleep(0.01)