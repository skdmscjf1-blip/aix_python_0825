

# # 원의 반지름을 입력받아
# # 원의 넓이를 출력하시오.
# length = int(input("반지름을 입력하세요."))
# pi = 3.14
# # pi * (length ** 2)
# result = pi * (length **2)
# # 원의 넓이 : 100cm2
# print("원의 넓이 : ",result)

# # 2 * pi * length
# result2 = 2 * pi * length
# # 원의 둘레 : cm
# print("원의 둘레 : {:.2f}".format(result2))



# a = 10
# a = a + 2
# a += 2
# print(a)



# print("101"+"102") #101102
# print("안녕"+"하세요") #안녕하세요



# #번호,이름,국어,영어,수학을 입력받아
# #번호,이름,국어,영어,수학,합계,평균을 출력하시오

# #홍길동
# number = int(input("번호를 입력하세요."))
# name = input("이름을 입력하세요.")
# a = int(input("국어점수를 입력하세요."))
# b = int(input("영어점수를 입력하세요."))
# c = int(input("수학점수를 입력하세요."))

# sum = a+b+c
# avg = sum/3

# #유관순

# number2 = int(input("번호를 입력하세요."))
# name2 = input("이름을 입력하세요.")
# a2 = int(input("국어점수를 입력하세요."))
# b2 = int(input("영어점수를 입력하세요."))
# c2 = int(input("수학점수를 입력하세요."))

# sum2 = a2+b2+c2
# avg2 = sum2/3


# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("-"*60)
# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
#       format(number,name,a,b,c,sum,avg))

# print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".\
#       format(number2,name2,a2,b2,c2,sum2,avg2))
# print("-"*60)


# # 산술연산자 : +,-,*,/,//,%,**
# # 산술계산 : *,/ 먼저 +,- 순으로 진행
# # 우선순위에 있는 것은 괄호로 분리
# print(2+2-((2*2)/2)*2) #0
# print(2-2+2/2*2+2) #4


# #다른 타입 사칙연산 에러
# # print("안녕"+3) #에러
# print(1.1+5) #숫자타입 가능6.1
# print(int(1.9)) # 1 실수형을 정수형으로 변경시 소수점 사라짐


# ##문자열 덧셈연산(+), 반복연산(*)
# print("안녕"+"하세요.")   #연결
# print("안녕"*10)        #반복


# # 문자열 숫자인경우 > 문자열타입을 숫자타입으로 변경가능
# str1,str2,str3 = "100","1.123","999"
# # print(str1+1) #가능?? 불가능
# print(int(str1)+1) # 문자열숫자 자동변경안됨. int,float
# print(float(str2)) # 실수형타입으로 변경
# print(int(str3)+1)
# # print(int("안녕")) #문자를 숫자로 변환에러
