alist = list(range(1,26))
#print(alist)

for i in range(len(alist)) :
    if (i+1)%5!=0 :
        print (alist[i],end="\t")
    else :
        print(alist[i])
# 1       2       3       4       5
# 6       7       8       9       10
# 11      12      13      14      15
# 16      17      18      19      20
# 21      22      23      24      25




# # #1,25까지 리스트를 생성하고 
# # #랜덤으로 리스트를 섞음 다음, 5개씩 2차원 리스트를 만드시오.
=======
# alist = list(range(1,26))
# # print(alist)
# for i in range(len(alist)):
#     if (i+1)%5!=0:
#         print(alist[i],end="\t")
#     else:
#         print(alist[i])    


# # 1,25까지 리스트를 생성하고
# # 랜덤으로 리스트를 섞은 다음, 5개씩 2차원리스트를 만드시오.
# import random
# alist = list(range(1,26))
# random.shuffle(alist)
# alist2 =[]
# for i in range(0,len(alist),5) :
#         alist2.append(alist[i:i+5])
# print(alist2)#숫자 랜덤 
#[[11, 22, 3, 20, 18], [6, 5, 10, 1, 17], [7, 8, 12, 15, 16], [13, 4, 25, 2, 9], [19, 14, 24, 23, 21]]


# #문자열 3자리씩 끊어서 리스트로 작성하시오.
# aa= "abcdefabcdefabcdefabcdefabcdef"
# aa2 = []
# for i in range(0,len(aa),3) :
#     aa2.append(aa[i:i+3]) #0,1,2
# print(aa2) # ['abc', 'def', 'abc', 'def', 'abc', 'def', 'abc', 'def', 'abc', 'def']

#1차원리스트를 2차원형태로 구성
# arr = [1,2,3,4,5,6,7,8,9]

# alist2 = []
# for i in range(0,len(alist),5):
#     alist2.append(alist[i:i+5])  #0,1,2
# print(alist2) 
# # alist2 = [[],[],[],[],[]]



# 문자열을 3자리씩 끊어서 리스트로 저장하시오.
# aa = "abcdefabcdefabcdefabcdefabcdef" #30
# aa2 = [] # 3개씩 나눠서 저장하시오.
# for i in range(0,len(aa),3):
#     aa2.append(aa[i:i+3])  #0,1,2
# print(aa2)  



# 1차원리스트를 2차원형태로 구성
# arr = [1,2,3,4,5,6,7,8,9]  #len(arr) = 9
# arr2 = []
# for i in range(0,len(arr),3):
#     arr2.append(arr[i:i+3])  #0,1,2
# print(arr2)    

# for i in range(0,len(arr),3) :
#     arr2.append(arr[i:i+3]) #0,1,2
# print(arr2) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# arr2 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
