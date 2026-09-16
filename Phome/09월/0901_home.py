# # # 퀴즈
# n_arr = [100,91,230,1,2,5,70,500]
# # # 100이상의 숫자만 출력하시오.
# # # 100:3자리숫자
# # # 91:2자리숫자
# # # 230:3자리숫자
# # # 1:1자리숫자
# arr=[]
# for n in n_arr :
#     no =len(str(n))
#     a = "{} : {}자리숫자" .format (n,no)
#     arr.append(a)
# print(arr)



# stu_list = []
# while True : 
#     no = len(stu_list)+1
#     print("자동번호 : ",no)
#     name=input("이름입력 (종료하려면 0) :")
#     if name=="0" : break
#     kor = int(input("국어입력 : "))
#     eng = int(input("수학입력 : "))
#     math = int(input("영어입력 : "))
#     total = kor+eng+math
#     avg = total/3
#     stu_list.append([no,name,kor,eng,math,total,avg])

# print("입력된 학생 성적",len(stu_list))
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("*"*60)
# for s in stu_list : 
#     print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s))

# # # 로또맞추기
# # # 1. 랜덤번호 6개 중복되지않게 생성
# # # 2. 입력번호 6개 생성
# # # 3. 랜덤번호 와 입력번호 비교
# # # -for 입력번호 1개 가져와서 랜덤번호리스트와 비교
# # # - 있는 번호를 리스트에 추가
# # # 4. 결과 출력

# import random
# lotto = random.sample(range(1,46),6)
# print(lotto)
# mynum = []
# for i in range(6) :
#     no = int(input("숫자입력 : "))
#     mynum.append(no)

# answer = []
# for m in mynum : 
#     if m in lotto :
#         answer.append(m)
# print("로또번호 : ",lotto)
# print("입력번호 : ",mynum)
# print("정답개수 : ",len(answer))
# print("정답번호 : ",answer)



# #구구단
# for i in range(2,10):
#     for j in range(1,10) :
#         print("{}X{}={}".format(i,j,i*j))

#         # 1-100사이의 숫자맞추기
# # 1. 랜덤번호 1개 생성
# # 2. 무한으로 입력받기
# # 3. 숫자를 입력받기 
# # 4. 랜덤번호와 숫자 비교 
# # 5. 결과출력

# import random
# ran = random.randint(1,100)
# arr = []
# while True :
#     no = int(input("1-100사이 숫자를 입력하세요 : "))
#     arr.append(no)
#     if no==ran :
#         print("정답!")
#         break
#     elif no>ran :
#         print(no,"보다 작은수 입력!")
#     else:
#         print(no,"보다 큰수 입력!")

# print("입력한 모든 숫자 : ",arr)
# print("정답 : ",ran)