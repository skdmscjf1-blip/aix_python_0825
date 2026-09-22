#반복문을 사용해서 1-100까지 합을 출력하시오

#200을 넘는 시점의 i의 값과 i번째 합계를 출력하시오

#200을 넘는 이전 시점의 i,합계를 출력하시오.

# 구구단을 출력하시오

# sum = 0
# for i in range(1,101):
#     sum= sum+i
# print(sum)

# sum = 0
# for i in range(1,50) :
#     sum = sum+i
#     if sum >=200 :
#         break
# print(f"{sum},{i}")

# sum1 = 0
# for i in range(1,50) :
#     sum1 = sum1+i
#     if sum1>=200 :
#         break
# print("200넘기전 합계",sum1-i)
# print("200넘기전 i ",i-1)


# for i in range(2,10) :
#     for j in range(1,10) :
#         print(f"{i} X {j} = {i*j}")

# name = []
# kor = []
# for i in range(2) :
#     name.append(input("이름입력 : "))
#     kor.append(int(input("국어점수 : ")))

# for i in range(2) :
#     print("{}\t{}".format(name[i],kor[i]))

# stu = []
# for i in range(2) :
#     no = i+1
#     name = input("이름입력 : ")
#     kor = int(input("국어점수 입력 : "))
#     stu.append([no,name,kor])
# for i in range(2) :
#     print("{}\t{}\t{}\t".format(stu[i][0],stu[i][1],stu[i][2]))