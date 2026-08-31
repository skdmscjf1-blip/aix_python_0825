# ## 1-100사이의 랜덤 번호를 맞추는 프로그램을 구현하시오.
# #랜덤번호보다 높은 수를 입력하면 낮은 숫자입력!!,높은 숫자입력!
# #정답을 맞추면 
# #정답숫자 :
# #숫자입력회수 :
# #입력한 숫자 :

# import random
# ran1 = random.randint(1,100)

# my_list =[]
# myNum= []
# answer = 0
# while True :
#     myNum = int(input("숫자입력 : "))
#     my_list.append(myNum)
#     if myNum == ran1 :
#         answer = myNum
#         print("정답입니다.")
#         break
#     elif myNum > ran1 :
#         print("입력한 숫자가 더 큽니다. 작은수 입력!!")
#     else :
#         print("입력한 숫자가 더 작습니다. 큰수 입력!!")

# print("정답 : ",answer)
# print("숫자입력횟수 : ",len(my_list))
# print("입력한 숫자 : ",my_list)


import random
lotto = random.sample(range(1,46),6)
print(lotto)

i = 0
my_list = []
#입력부
while i<6 :
    no = int(input("숫자입력"))
    if no not in my_list :
        my_list.append(no)
        i = i+1
    else :
        print("숫자가 중복됩니다. 다시 입력하세요 : ")

count = 0
answer = []

for i in my_list :
    if i in lotto :
        count = count+1
        answer.append(i)

print("lotto 번호",lotto)
print("내 로또 입력번호 : ",my_list)
print("당첨숫자" ,answer)
print("당첨숫자 갯수" ,count)