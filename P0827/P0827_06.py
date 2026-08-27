import random

random_no = random.randint(-10,10)
print("랜덤숫자 : ",random_no)

if random_no>0:
    print("양수")
else:
    print("음수")

#랜덤숫자가 양수,음수인지 출력하시오.


# #조건문을 여러개
# score = 65
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("F")



#조건문안에 조건문
# a = 1
# if a>50:
#     if a<100:
#         print("50보다크고,100보다 작은수")
#     else:
#         print("50보다크고,100보다 큰수")
# else:
#     print("50보다 작은수")