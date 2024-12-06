from selenium import webdriver
from time import sleep
loop = input("업데이트 할 초성을 공백 없이 적어주세요. 전체 업데이트는 아무것도 적지 말고 넘겨주세요: ")
if loop=='':
    loop="ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ"
else:
    for i in loop:
        if i in "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ":
           continue
        else:
            print("잘못 입력하셨습니다.")
            exit()
location = input("파일을 저장할 디렉터리의 이름을 적어주세요. 현재 위치에 저장하려면 '.'을 입력하세요: ")
# 웹 드라이버 초기화
driver = webdriver.Chrome()  # 크롬 드라이버 예시
# 페이지 소스 코드 가져오기
def extract(string, index):
    return string[index+2:string.find("</a></td>")]

for k in loop:
    driver.get("https://kkukowiki.kr/w/긴_단어/한국어/"+k)  # 원하는 URL로 이동
    sleep(1)
    line = driver.page_source.splitlines()
    
    for i in line:
        if "<h2><span id=" in i:
            file=open(location+"/"+i[14]+".txt", "w", encoding="utf-8")
            continue
        else:
            index = i.find('\">')
            if index!=-1 and "</a></td>" in i:
                file.write(extract(i,index)+"\n")
            else: continue
driver.quit()
