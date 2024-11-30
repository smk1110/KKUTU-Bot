from selenium import webdriver
from time import sleep
# 웹 드라이버 초기화
driver = webdriver.Chrome()  # 크롬 드라이버 예시
# 페이지 소스 코드 가져오기
def extract(string, index):
    return string[index+2:string.find("</a></td>")]
loop = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ"
for k in loop:
    driver.get("https://kkukowiki.kr/w/긴_단어/한국어/"+k)  # 원하는 URL로 이동
    sleep(1)
    line = driver.page_source.splitlines()
    
    for i in line:
        if "<h2><span id=" in i:
            file=open("Text_files/"+i[14]+".txt", "w", encoding="utf-8")
            continue
        else:
            index = i.find('\">')
            if index!=-1 and "</a></td>" in i:
                file.write(extract(i,index)+"\n")
            else: continue
driver.quit()
