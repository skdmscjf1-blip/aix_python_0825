#람다식 - 함수요약
#함수사용
# def sum(n1,n2) :
#     result =n1+n2
#     return result

# print(sum(10,20)) # 30

#람다식 - 1줄만 명령어가 있어야 함.
# sum = lambda n1:n1+10
# print(sum(10)) #20

# #map (함수,리스트)
# mList = [1,2,3,4,5] #+10

#기본구성
# mList2 = []
# for m in mList :
#     mList2.append(m+10)

# def add(num):

#     return num+10

# mList = [1,2,3,4,5]
# a_arr = []
# for m in mList:
#     a_arr.append(add(m))


#리스트내포
# a_arr = [m+10 for m in mList]
# print(a_arr)

#map

# def add(num):
#     return num+10

# map -> amp(함수,리스트)
# a_lam = lambda num : num+10
# mList = [1,2,3,4,5]
# mList2 = list(map(lambda num:num+10,[1,2,3,4,5])) ********************중요
# print(mList2)

# 문자열리스트 -> 숫자리스트로 변경
# data = ["100","200","300"]
# result = map(int,data)
# print(result) # 안찍힘
# print(list(result)) #리스트로 받아야함

#
# a = [1,2,3]
# b = [10,20,30]
# result = map(lambda x,y:x+y,a,b)   *********중요
# print(list(result)) # [11,22,33]

# 1-4 곱을 구하시오.
# result = 1
# for i in range(1,5) :
#     result = result*i
# print(result) #24

# #----------------------
# #재귀함수 -  자기자신함수를 다시 호출
# def fact1(num):
#     if num<=1: return num
#     else : return num * fact1(num-1)

# print(fact1(4)) #24





