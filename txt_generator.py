#For automation level 3
target='<h2><span id="'
file_name= "ㄷ.html"
folder_name="Text_files" #띄어쓰기 안 됨
lines=[]
f = open(file_name, "r",encoding='utf-8')
while True:
    text = f.readline()
    index=text.find(target)
    if index!=-1:
        word=text[index+len(target)]
        print(word)
        g = open(".\\"+folder_name+"\\"+word+".txt", "w",encoding='utf-8')
        while True:
            text=f.readline()
            title_index=text.find("<td><a")
            if title_index==0:
                content = text[text.find("\">")+2: text.find("</a></td>")]
                g.write(content+"\n")
            elif "</table>" in text:
                g.close()
                break
    elif "<!--" in text:
        if "NewPP" in f.readline():
            break

    

    

        