# r : 파일읽기 , w : 파일덮어쓰기 , a:이어쓰기

with open("c:/aaa/abc.txt","a") as f:
    while True :
        line = input("글을 입력하세요. : ")
        if line != "" :
            f.writelines(line+"\n")
        else : 
            break

print("파일이 저장되었습니다.") 
