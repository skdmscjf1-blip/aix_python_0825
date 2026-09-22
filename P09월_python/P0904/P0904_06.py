# test2.txt 파일을 읽어와서
#stu = []
#데이터를 리스트에 저장하시오
stu = []
#with : f.close() 생략가능
with open("C:/aaa/test2.txt","r",encoding="utf-8") as f:
    while True :
        line = f.readline()
        if line=="": break
        line = line.strip()
        arr = line.split(",")
        print(arr)
        for i,a in enumerate(arr) :
            if 5>=i>=2:
                arr[i] = int(a)
            elif i==6:
                arr[i] = float(a)
        stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})
        

print(stu)