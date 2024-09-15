#텍스트 파일을 이미 영타로 변환했을 때 변환 과정을 생략한 프로그램입니다.
#완전한 형태의 한글만 가능합니다. (ㄱ, ㄴ, ㅓ, 등 불가)
import keyboard
import time
splited = []
def split(a):
    global splited
    for i in a:
        splited.append(i)
while True:
    key = keyboard.read_key()
    print(key)
    if key == 'esc':
        time.sleep(0.5)
        while True:
            if keyboard.is_pressed('esc'):
                time.sleep(0.5)
                break
    else:
        splited = []
        try:
            file = open("Bookmarks\\"+key+".txt", 'r', encoding='utf-8')
        except FileNotFoundError:
            continue
        text=file.readline()
        split(text)
        keyboard.send('backspace')
        for j in splited:
            if j.isupper():
                keyboard.press_and_release('shift + '+j.lower())
            else:
                keyboard.press_and_release(j)
            time.sleep(0.01)
