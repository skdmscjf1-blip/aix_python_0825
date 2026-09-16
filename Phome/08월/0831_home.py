
# import random
# ran = random.randint(1,100)
# mylist=[]
# while True : 
#     mynum = int(input("숫자입력 : "))
#     mylist.append(mynum)
#     if mynum==ran :
#         print("정답입니다!")
#         break
#     elif mynum>ran :
#         print("입력한 숫자가 더 큽니다! 작은 수 입력 :")
#     else :
#         print("입력한 숫자가 더 작습니다! 큰 수 입력 : ")

# print("정답 : ",ran)
# print("숫자입력횟수 : ",len(mylist))
# print("입력한 숫자",mylist)

import random
lotto = random.sample(range(1,46),6)
print(lotto)

mynum = []
i = 0
while i<6:
    no = int(input("번호를 입력하시오."))
    if no not in mynum : 
        mynum.append(no)
        i = i+1
    else : 
        print("번호가 있습니다.")
#맞는지 확인
count = 0
answer = []
for i in mynum : 
    if i in lotto :
        count = count + 1
        answer.append(i)

print("로또번호 : ",lotto)
print("입력번호 : ",mynum)
print("정답번호 : ",answer)
print("정답개수 : ",count)



# #두수를 입력받아 합을 구하는 무한반복 프로그램을 구현하시오.

# while True : 
#     a = int(input("1.숫자 : "))
#     if a==0 : break
#     b = int(input("2.숫자 : "))
#     if b==0 : break
#     print(f"{a}+{b}={a+b}")
# print("프로그램 종료")

# alist = []
# print(len(alist))
# alist2 = [0,0,0] #3개
# print(len(alist2))
# alist3 = [0]*10
# print(len(alist3))
# alist4 = list(range(10)) # 0,1,2,3,4,5.....
# print(alist4)
# alist5 = [i*i for i in range(10)] #리스트 내포
# print(alist5)


# # 입력한 첫번째 숫자부터 두번째 입력한 숫자까지 합을 구하시오.
# # 2 , 5
# sum = 0

# a=int(input("숫자입력: "))
# b=int(input("숫자입력: "))
# if a>b :
#     a,b=b,a
# for i in range(a,b+1) : 
#     sum = sum+i
# print("합 : ",sum)

sum = 0

# # 구구단 5단만 출력

# a = int(input("숫자입력 : "))
# b = int(input("숫자입력 : "))
# for i in range(a,10) :
#     for j in range(1,b+1) :
#         print(f"{i}X{j}={i*j}")


# list_a = ["바나나","딸기","사과","배","복숭아"]
# for i in range(len(list_a)) : 
#     print(i+1,":",list_a[i])

# #enumerate : index번호,리스트값 2개 전달
# list_a = ["바나나","딸기","사과","배","복숭아"]
# for i,v in enumerate(list_a) :
#     print(i+1,":",v)


# list_a = ["바나나","딸기","사과","배","복숭아"]
# j=1
# for i in list_a :
#     print(j,":",i)
#     j = j+1

# name=[]
# kor = []
# eng = []
# math = []
# total = []
# avg = []
# for i in range(3) :
#     name.append(input("이름입력 : "))
#     k_input = int(input("국어점수 입력: "))
#     kor.append(k_input)
#     e_input = int(input("영어점수 입력: "))
#     eng.append(k_input)
#     m_input = int(input("수학점수 입력: "))
#     math.append(k_input)
#     total.append(k_input+e_input+m_input)
#     avg.append((k_input+e_input+m_input)/3)

# print("[학생성적]")
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("*"*60)
# for i in range(len(name)) :
#     print(f"{i+1}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\t{total[i]}\t{avg[i]:.2f}")



# # 입력한 숫자가 홀수인지,짝수인지 출력하시오.
# a= int(input("숫자입력 : "))
# if a%2==0 :
#     print("짝수입니다")
# else :
#     print("홀수입니다.")


# nums = [3,9,10,105,220,2,1]
# for n in nums :
#     #a = int(input("숫자입력: "))
#     if n%2==0 :
#         print(n,"짝수입니다.")
#     else : pass
#         #print(n,"홀수입니다.")

# # 구구단 출력
# for i in range(2,10) :
#     print(f"[{i}]단")
#     for j in range(1,10) :
#         print("{}X{}={}".format(i,j,i*j),end="\t")
#     print()

# #구구단 출력
# for i in range(2,10) :
#     for j in range(1,10) :
#         print("{}X{}={}".format(i,j,i*j))