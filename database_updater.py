from selenium import webdriver

# 웹 드라이버 초기화
driver = webdriver.Chrome()  # 크롬 드라이버 예시
# 페이지 소스 코드 가져오기
def extract(string, index):
    return string[index+2:string.find("</a></td>")]
loop = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ"
for k in loop:
    driver.get("https://kkukowiki.kr/w/긴_단어/한국어/"+k)  # 원하는 URL로 이동
    line = driver.page_source.splitlines()
    i=-1
    while i<len(line)-10:
        i+=1
        string = line[i]
        if "<h2><span id=" in string:
            file=open("Text_files/"+string[14]+".txt", "w", encoding="utf-8")
            while True:
                i+=1
                string = line[i]
                index = string.find('\">')
                if index!=-1 and "</a></td>" in string:
                    file.write(extract(string,index)+"\n")
                elif '</td></tr></tbody><tfoot></tfoot></table>' in string:
                    break
        elif "NewPP limit report" in string:
            break

driver.quit()
