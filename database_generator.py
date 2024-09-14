starting_word=input("Starting word :")
title = input("Title : ")
command = input("Command : ")
file_name= ""
lines=[]
f = open(file_name, "r",encoding='utf-8')
while True:
    text = f.readline()
    if "<span id=\""+starting_word+"\">" in text:
        lines.append(text)
        break
while True:
    a=f.readline()
    b=a.find(" href")
    if b==-1:
        lines.append(a)
    else:
        c=a.find(">", b)
        lines.append(a.replace(a[b:c],''))
    d=a.find("<!--")
    if d!=-1:
        break
f = open(file_name, "w",encoding='utf-8')
f.write("<!DOCTYPE html>\n")
f.write('<html class="client-js" lang="ko" dir="ltr"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n')
f.write("<title>"+title+"</title>\n")
for line in lines:
    f.write(line)
f.write(command)
f.write("-->\n")
f.write("</body></html>\n")
f.close()

    

    

        