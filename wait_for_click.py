import mouse

# 마우스 클릭을 기다리는 함수
def main():
    mouse.on_click(lambda: print("Mouse clicked") or mouse.unhook_all())

    # 마우스 클릭이 발생할 때까지 이벤트를 계속 감지합니다.
    mouse.wait(button='left', target_types=('down',))
