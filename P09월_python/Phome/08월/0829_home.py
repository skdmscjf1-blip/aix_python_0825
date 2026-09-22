
# 13일차 문제
# 1. 2
# 2. 2
#3. 3
#4. 3
#5. 2
#6. 2
#7. 3
#8. 2
#9. 3
#10. 
exercise = [20,60,40,10,80,50]

count = 0
for i in exercise :
    if i>=40 :
        count = count +1
print(count)
    







# #12일차 문제
# # 
# # 1. 3
# # 2. 2
# # 3. 3
# # 4. 3
# # 5. 2
# # 6. 3
# # 7. 2
# # 8. 2
# # 9. 2
# # 10.  
# # exercise = ["필라테스","러닝","필라테스","수영","러닝","필라테스"]
# # exercise = set(exercise)
# # print(exercise)






# # 9일차 문제
# #1. 2
# #2. 3
# #3. 2
# # 4. 3
# # 5. 3
# # 6. 3
# # 7. 3
# # 8. 3
# # 9. 3
# # 10 . 

# def add_ten(add):
#     return add+10

# result = add_ten(20)
# print(result)

    




# # scores = [90,50,80,40,100]

# # def check_score(score) :
# #     if score>=60:
# #         return "합격"
# #     else:
# #         return "불합격"
# # for score in scores :
# #     print(score,check_score(score))



# # def check_score(score) : 
# #     if score>=80:
# #         return "합격"
# #     else : 
# #         return "불합격"
# # result = check_score(79)
# # print(result)
    


# # def calculate_bmi(weight,height):
# #     bmi = weight / (height**2)
# #     return bmi

# # result = calculate_bmi(60,1.65)
# # print(result)


# # def add(a,b):
# #     result = a+b
# #     return result
# # answer = add(10,20)
# # print(answer)


# # def hello(name,age) : 
# #     print("이름",name)
# #     print("나이",age)

# # hello("은철",37)



# # def hello():
# #     print("안녕하세요")

# # hello()

# # # def : define (정의하다) , 새로운 기능을 만든다.
# # def bmi() : 
# #     weight = 70
# #     height = 1.75
# #     result = weight / (height**2)
# #     print(result)
# # bmi()

# # # 8일차 문제
# # # 1. 2
# # # 2. 2
# # # 3. 3
# # # 4. 3
# # # 5. 2
# # # 6. 2
# # # 7. 3
# # # 8. 2
# # # 9. 2
# # # 10. 
# # member = {
# #     "name" : "영희",
# #     "age"  : 32,
# #     "high" : 165.5
# # }
# # del member["age"]
# # print(member)




# # members = [
# #     {"name": "철수","age" : 31},
# #     {"name": "영희","age" : 34},
# #     {"name": "빡구","age" : 35},
# # ]
# # for member in members :
# #     print(member["name"])

# # member ={"name" : "영희",
# #          "age" : 32
# # }
# # member["age"] = 33
# # print(member)
# # member["weight"] = 60.9
# # print(member)
# # del member["weight"]
# # print(member)


# #리스트 안에 리스트 만들어서 성적 출력해보기

# # arr = []

# # for i in range(2) : 
# #     no = i+1
# #     a = input("이름을 입력하세요 : ")
# #     b = int(input("수학점수를 입력하세요 : "))
# #     arr.append([no,a,b])
# # for i in range(2) : 
# #     print("{}\t{}\t{}\t".format(arr[i][0],arr[i][1],arr[i][2]))



# #리스트안에 리스트로 만들어보기.
# # stu = []

# # for i in range(2) : 
# #     no = 1+i
# #     name = input("이름을 입력하세요 : ")
# #     kor = int(input("국어점수를 입력하세요 : "))
# #     stu.append([no,name,kor])
# # print(stu)

# # for i in range(2):
# #     print("{}\t{}\t{}".format\
# # (stu[i][0],stu[i][1],stu[i][2]))
    

# # 리스트로 이름,국어점수 만들기
# # name = []
# # kor = []

# # for i in range(2) :
# #     name.append(input("이름을 입력하세요 : "))
# #     kor.append(int(input("국어점수를 입력하세요 : ")))
# # for i in range(2) : 
# #     print(f"{name[i]}\t{kor[i]}")


# # #합계가 100이 넘어가기 전 i 는 얼마?

# # sum = 0
# # for i in range (1,50) :
# #     sum =sum+i
# #     if sum>=100 :
# #         break
# # print("합계 100 넘기전 값 : ",sum-i)
# # print("합계 100 넘기전 시점 : ",i-1)


# # #합계가 100이 넘어가는 시점은 i 가 얼마?
# # sum = 0
# # for i in range(1,50) :
# #     sum = sum + i
# #     if sum>=100 :
# #         break
# # print("합계가 100이 넘어가는 시점 : ",i)
# # print("합계 100 넘음 : ",sum)
      

# # # 2단

# # for i in range(1,10):
# #         print(f" 2 X {i} = {2*i} ")

# # #구구단

# # for i in range(1,10) : 
# #     for j in range(1,10) :
# #         print(f"{i}X{j} = {i*j}")