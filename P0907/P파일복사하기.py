#파일복사하기
import os


rf = open("c:/aaa/123.jpg","rb") #rb 읽기
wf = open("c:/aaa2/234.jpg","wb") # wb 쓰기

while True :
    fdata = rf.read(1)
    if not fdata : break
    wf.write(fdata)

rf.close()    
wf.close()
print("이미지파일이 복사되었습니다.")    

# rf = open("c:/aaa/1.jpg","rb")
# wf = open("c:/aaa2/2.jpg","wb")

# while True :
#     fdata = rf.read(1)
#     if not fdata : break
#     wf.write(fdata)

# rf.close()
# wf.close()
# print("이미지파일이 복사되었습니다.")