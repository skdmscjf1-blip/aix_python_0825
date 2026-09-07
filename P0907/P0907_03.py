m_str = '"서울특별시  (1100000000)","9,330,658","4,482,949","          2.08","4,504,432","4,826,226","          0.93"'

with open("common/stu.txt","a",encoding="utf-8") as f:
    allStr = ""
    no = 0
    while True:
        outStr = input("내용입력 : ")
        if no==0 : 
            allStr=outStr
            no+=1
            continue
        if outStr == "":
            f.write(allStr+"\n")
            break
        allStr += (","+outStr)
        no+=1
    print(allStr)
