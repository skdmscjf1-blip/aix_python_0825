#리스트 안에 리스트 만들어서 성적 출력해보기

# arr = []

# for i in range(2) : 
#     no = i+1
#     a = input("이름을 입력하세요 : ")
#     b = int(input("수학점수를 입력하세요 : "))
#     arr.append([no,a,b])
# for i in range(2) : 
#     print("{}\t{}\t{}\t".format(arr[i][0],arr[i][1],arr[i][2]))



#리스트안에 리스트로 만들어보기.
# stu = []

# for i in range(2) : 
#     no = 1+i
#     name = input("이름을 입력하세요 : ")
#     kor = int(input("국어점수를 입력하세요 : "))
#     stu.append([no,name,kor])
# print(stu)

# for i in range(2):
#     print("{}\t{}\t{}".format\
# (stu[i][0],stu[i][1],stu[i][2]))
    

# 리스트로 이름,국어점수 만들기
# name = []
# kor = []

# for i in range(2) :
#     name.append(input("이름을 입력하세요 : "))
#     kor.append(int(input("국어점수를 입력하세요 : ")))
# for i in range(2) : 
#     print(f"{name[i]}\t{kor[i]}")


# #합계가 100이 넘어가기 전 i 는 얼마?

# sum = 0
# for i in range (1,50) :
#     sum =sum+i
#     if sum>=100 :
#         break
# print("합계 100 넘기전 값 : ",sum-i)
# print("합계 100 넘기전 시점 : ",i-1)


# #합계가 100이 넘어가는 시점은 i 가 얼마?
# sum = 0
# for i in range(1,50) :
#     sum = sum + i
#     if sum>=100 :
#         break
# print("합계가 100이 넘어가는 시점 : ",i)
# print("합계 100 넘음 : ",sum)
      

# # 2단

# for i in range(1,10):
#         print(f" 2 X {i} = {2*i} ")

# #구구단

# for i in range(1,10) : 
#     for j in range(1,10) :
#         print(f"{i}X{j} = {i*j}")



# ##번호표 001

# for i in range(0,10):
#     for j in range(0,10) : 
#         for k in range(0,10) :
#             print(f"{i}{j}{k}") 


# for i in range (0,10) :
#     for j in range (0,10) :
#         for k in range(0,10) :
#                 print((i*100)+(j*10)+k+1,":",i,j,k)


# for i in range(1,10):
#     print(f"2 x {i} = {i*2}")




# sum = 0
# for i in range(1,11):
#     sum = sum+i
# print("합계 : ",sum)

# sum = 0
# for i in range(1,11):
#     sum = sum+i
#     if sum>=11:
#         print("10보다 크기 바로앞일때",i-1)
#         print("10초과전 시점 : ",sum-i)
#         break
   

# for i in range(3):
#     no = i+1
#     a = input("이름입력 : ")
#     b = int(input("국어점수 입력 : "))
#     c = int(input("영어점수 입력 : "))
#     print(f"{no}\t{a}\t{b}\t{c}")

# for i in range(5):
#     print(i)

# for i in range(0,5):  
#     print(i*10)  

# for i in range(0,10,2):
#     print(i)  

# for i in [1,5,3,2]:
#     print(i)  


# for i in "안녕하세요":
#     print(i) 


# arr = list(range(1,11))          
# print(arr)

# import random
# arr = random.sample(range(1,46),5) #1-45까지 중복없이 5개를 가져옴.
# print(arr)
# arr2 = random.sample([1,2,3],2)
# print(arr2)
# arr3 = [1,2,3,4,5]  # 리스트 전체를 랜덤으로 섞어줌.
# random.shuffle(arr3)
# print(arr3)
# arr4 = [1,2,3,4,5]
# arr5 = random.choices(arr4,k=5) # 리스트 해당개수만큼 가져옴.중복가능
# print(arr5)



# lotto = random.sample(range(1,46),5)
# print(lotto)
# arr = []

# for i in range(5):
#     arr.append(int(input("숫자를 입력하시오 : ")))
# for i in range(5):
#     if arr[i] in lotto :
#         print("당첨")
#     else:
#         print("꽝")


# a = [1,2,3,4,5]
# print(a)
# a[2]=30
# a[3]=500
# print(a)
# a.pop(2)
# print(a)
# a.append(200)
# print(a)




# name = input("이름을 입력하세요 : ")
# if name.isalpha():
#     print("문자,알파벳으로 되어 있습니다.")
# else:
#     print("특수문자나 숫자가 입력되었습니다")
# print(name)

# name = input("이름입력 : ")
# while(True) : 
#     kor = input("국어점수 입력 : ")
#     if kor.isdigit():
#         kor = int(kor)
#         break
#     else:
#         print("숫자가 아닙니다.다시 입력해주세요")
# print(name,kor)


# print("[ 로그인페이지 ]")

# while(True):
#     id = input("아이디 : ")
#     pw = input("패스워드 : ")
#     if id=="aaa" and pw=="1111":
#         print("로그인 성공!")
#         break
#     else:
#         print("아이디 또는 패스워드가 일치하지않습니다. 다시 로그인해 주세요")

# print("메인페이지가 열립니다")


# paper = "네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서\
#      2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다.\
#       이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서\
#            비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."

# result1 = paper.rfind("홍수")
# print(result1)

# result2 = paper.count("홍수")
# print(result2)



# result1 = paper.find("홍수")
# print(result1)
# result2 = paper.find("홍수",5)
# print(result2)


# #번호,이름,국어,영어,수학,합계,평균을 출력하시오

# str = "1,홍길동,100,100,99"
# s = str.split(",")
# print(s)
# s[2] =int(s[2])
# s[3] =int(s[3])
# s[4] =int(s[4])
# s.append(s[2]+s[3]+s[4])
# s.append(s[5]/3)

# print("[학생성적프로그램]")
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("*"*60)
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))



# a = [1,2,3,4,5]

# print(a)
# print(*a)
# print(a[0],a[1],a[2],a[3],a[4])

# #1inch = 2.54cm

# a = input("숫자입력 : ")
# a = int(a)
# b = a*2.54
# print("icnh : ",a)
# print("cm : ",b)


# cc = "aabbccddee"
# print(cc.upper())
# dd = "AaBbCcddee"
# print(dd.lower())

# #find

# b = "abcdefdghi"
# print(b.find("d"))
# print(b.rfind("d"))

# #replace
# a = "aabbccddeeff"
# a1 = a.replace("a","y")
# print(a1)

# #strip - 공백제거
# a = "    안녕하세요         "
# print(a)
# print(a.strip())


#문자열 함수
# split,strip,replace,find,rfind
# upper -영문자 모두 대문자로 출력 , lower - 소문자로 출력

# str1 = "1,홍길동,100,100,100,300,100" #문자열타입
# s = str1.split(",") # split 특정문자를 기준으로 분리를 해줌.
# print(s)
# print(s[2])
# str2 = "2026-08-28"
# s2 = str2.split("-")
# print(s2)
# print(s2[2])
# str3 = "안녕 반가워 다음에 봐"
# s3 = str3.split(" ")
# print(s3)
# print(s3[1])


# # 문자슬라이싱

# str = "안녕하세요"
# print(str[1])

# #[시작:끝:간격]
# print(str[::-1])
# print(str[:-1])
# print(str[::2])
# #print(str[10])
# print(len(str))


# s = [0,0,0,0,0,0,0]

# s[0] = input("번호 : ")
# s[1] = input("이름 : ")
# s[2] = int(input("국어 : "))
# s[3] = int(input("영어 : "))
# s[4] = int(input("수학 : "))
# s[5] = s[3]+s[4]+s[5]
# s[6] = s[5]/3

# print("[학생성적프로그램]")
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("*"*60)
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))