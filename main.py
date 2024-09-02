import keyboard
import time
import hangul_to_english
number = 5
splited = []
with open(str(number)+".txt", 'r', encoding='utf-8') as file:
    while True:
        hangul_text = file.read(1)  # 한 글자씩 읽기
        if not hangul_text:  # 파일의 끝에 도달하면 종료
            break
        splited.append(hangul_text)
for i in splited:
    hangul_to_english.main(i)
print(splited)
print(hangul_to_english.result)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)

for j in hangul_to_english.result:
    if j.isupper():
        keyboard.press_and_release('shift + '+j.lower())
    else:
        keyboard.press_and_release(j)
    time.sleep(0.01)