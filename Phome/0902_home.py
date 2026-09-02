
# bb = "100,10,5,4,1"
# # 모든수의 합을 구하시오.
# bb_list = bb.split(",")
# bb_list = [int(i) for i in bb_list]
# total = sum(bb_list)
# print(total)

# # a = ["바나나","딸기","사과","딸기","딸기","사과"]
# aa = [1,2,3,1,1,1,2,3,1,1,1,2,2,3]
# # print(aa.count("딸기"))
# # {"바나나":1,"딸기":3,"사과":2}
# aa_dict = {}
# for a in aa:
#     if a not in aa_dict :
#         aa_dict[a] = 1
#     else : 
#         aa_dict[a] = aa_dict[a] +1
# print(aa_dict)


# alist = list(range(1,26))
# for i in range(len(alist)) :
#     if (i+1)%5 !=0 :
#         print(alist[i],end="\t")
#     else :
#         print(alist[i])



# 1,25까지 리스트를 생성하고
# 랜덤으로 리스트를 섞은 다음, 5개씩 2차원리스트를 만드시오.
# import random
# arr = list(range(1,26))
# random.shuffle(arr)
# ran_arr = []

# for i in range(0,len(arr),5) :
#     ran_arr.append(arr[i:i+5])
# print(ran_arr)
    
    



# # 문자열을 3자리씩 끊어서 리스트로 저장하시오.
# aa = "abcdefabcdefabcdefabcdefabcdef" #30
# aa1=[]
# for i in range(0,len(aa),3):
#     aa1.append(aa[i:i+3])
# print(aa1)

# # 1차원리스트를 2차원형태로 구성
# arr = [1,2,3,4,5,6,7,8,9]  #len(arr) = 9
# arr2 = []
# for i in range(0,len(arr),3) :
#     arr2.append(arr[i:i+3])
# print(arr2)
