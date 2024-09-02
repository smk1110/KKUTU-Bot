#텍스트 파일을 이미 영타로 변환했을 때 변환 과정을 생략한 프로그램입니다.
#완전한 형태의 한글만 가능합니다.
import keyboard
import time
while True:
    key = keyboard.read_key()
    if key == 'esc': exit()
    else:
        splited = []
        try:
            with open(key+".txt", 'r', encoding='utf-8') as file:
                while True:
                    text = file.read(1)  # 한 글자씩 읽기
                    if not text:  # 파일의 끝에 도달하면 종료
                        break
                    splited.append(text)
        except FileNotFoundError:
            continue
        keyboard.send('backspace')
        for j in splited:
            if j.isupper():
                keyboard.press_and_release('shift + '+j.lower())
            else:
                keyboard.press_and_release(j)
            time.sleep(0.01)
