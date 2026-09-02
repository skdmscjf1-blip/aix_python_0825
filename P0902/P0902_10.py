

# import random
# ran=random.randint(1,101)
# arr = []
# while True :
#     no = int(input("1-100사이 숫자를 입력하세요."))
#     arr.append(no)
#     if no==ran :
#         print("정답입니다!")
#         break
#     elif no>ran :
#         print(no,"보다 작은수 입력!")
#     else :
#         print(no,"보다 큰수 입력!")

# print("입력한 숫자 : ",arr)
# print("정답 : ",ran)


def cal(num1,num2,str1) : 
    result = 0
    if str1=="+" :
        result = num1+num2
    elif str1 == "-" :
        result = num1-num2
    elif str1=="*" :
        result = num1*num2
    elif str1=="/" :
        result = num1/num2
    return result


num1 = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))
str1 = input("+,-,*,/ 입력하세요.")
result = cal(num1,num2,str1)
print("결과값 : ",result)
