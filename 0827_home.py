
# 슬라이싱 [시작:끝:간격]
arr = [1,2,3,4,5,6,7,8,9]
print(arr[::2])
print(arr[1::2])
print(arr[:-1])  #마지막 제외 / 중요
print(arr[::-1]) #리스트 역순정렬

# fruit = ["사과","수박","딸기","참외","복숭아"]
# print(fruit[2]) # "딸기"
# print(fruit[1:4]) # 1,2,3 "수박","딸기","참외"
# print(fruit[2:]) # 2, 끝까지 출력
# print(fruit[:3]) # 처음부터 , 3앞에 까지 출력
# print(fruit[:]) # 모두출력
# print(fruit[::2]) # 2칸띄고 출력

# name = "안녕하세요반갑습니다."
# print(name)
# print(name[1]) 
# print(name[6])
# print(name[5:8]) #중요
# print(name[::-1]) #중요
# print(name[::2]) #중요

# arr = [1,2,3,9,5]
# # # insert : 원하는 위치에 추가
# arr.insert(1,20)
# print(arr)

# # # 리스트 삭제 - del , pop , remove, clear(모두삭제)

# arr = [1,2,3,4,5,True,"안녕"]
# #arr.pop(2)
# #del arr[0]

# arr.remove("안녕")
# print(arr)

#정렬 순차정렬(sort) , 역순정렬 sort(reverse=True)

# arr = [1,5,9,3,2,15,10]
# #arr.sort()
# arr.sort(reverse=True)
# print(arr)

# # # 랜덤점수를 생성해서
# # # 90-92점 A-, 93-97 A, 98 A+
# # # 80-82점 B-, 83-87 B, 88 B+
# # # 70-72점 C-, 73-77 C, 78 C+
# # # 랜덤점수 출력하시오.

# import random
# num = random.randint(0,100)

# if num>=90:
#     if num>=98:
#         print("A+")
#     elif num>=93:
#         print("A")
#     else :
#         print("A-")
# elif num>=80:
#     if num>=88:
#         print("B+")
#     elif num>=83:
#         print("B")
#     else:
#         print("B-")
# elif num>=70:
#     if num>=78:
#         print("C+")
#     elif num>=73:
#         print("C")
#     else :
#         print("C-")
# else :
#     print("F")

# print("랜덤점수 : ",num)

# #해당월에 따라 봄,여름,가을,겨울이라고 출력하시오.
# #겨울 12,1,2 봄 3,4,5 여름 6,7,8 가을 9,10,11
# #비교문을 사용해서
# #해당월 계절을 출력하시오

# import datetime
# now = datetime.datetime.now()

# month = now.month
# month = int(input("월을 입력하세요"))

# if month==12 or 2>=month>=1:
#     print("겨울입니다")
# elif 5>=month>=3:
#     print("봄입니다")
# elif 8>=month>=6:
#     print("여름입니다")
# else:
#     print("가을입니다.")
# print("몇월 : ",month)


# # # score 60점이상이면 합격,불합격

# score = int(input("점수를 입력하시오"))

# # if score>=60: print("합격!")
# # else: print("불합격!")

# result = "합격" if score>=60 else "불합격"
# print(result)


# #현재시간

# import datetime
# now = datetime.datetime.now()

# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)


# #1월에서 6월까지는 상반기
# #7월에서 12월까지는 하반기
# #상반기,하반기인지 출력하시오.

# import datetime
# now = datetime.datetime.now()
# month = now.month

# if month>=7:
#     print("{}월 : 하반기".format(month))
# else:
#     print("{}월 : 상반기".format(month))


# # 1~5 랜덤숫자를 출력하시오.
# import random
# num = random.randint(1,5)

# a = int(input("1~5까지 범위이 숫자를 입력하세요."))
# b = int(input("1~5까지 범위이 숫자를 입력하세요."))

# print("랜덤숫자 :",num)
# print("입력숫자 : ",a)
# print("입력숫자 : ",b)

# if num==a or num==b:
#     print("당첨!")
# else:
#     print("낙첨!")

# # #a,b 를 입력받아 
# # #합계가 100 넘으면 100보다큰수, 100보다작은수 라고 출력하시오.

# a = int(input("숫자를 입력하시오."))
# b = int(input("숫자를 입력하시오."))

# total = a+b

# if total>=100:
#     print("100보다 큰수")
# else:
#     print("100보다 작은수")
# print("a :{},b :{},합계 :{}".format(a,b,total))


# # # 학생 2명의 성적을 입력받아 출력하시오.
# # # 번호, 이름, 국어,영어,수학 점수를 입력받아
# # # 번호, 이름, 국어,영어,수학,합계,평균을 출력하시오

# no = input("번호 : ")
# name = input("이름 : ")
# a = int(input("국어점수 : "))
# b = int(input("영어점수 : "))
# c = int(input("수학점수 : "))

# total = a+b+c
# avg = total/3

# no2 = input("번호 : ")
# name2 = input("이름 : ")
# a2 = int(input("국어점수 : "))
# b2 = int(input("영어점수 : "))
# c2 = int(input("수학점수 : "))

# total2 = a2+b2+c2
# avg2 = total2/3
# print("*"*60)
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("*"*60)
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(no,name,a,b,c,total,avg))
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(no2,name2,a2,b2,c2,total2,avg2))
# print("*"*60)