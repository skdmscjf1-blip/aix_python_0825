with open("C:\\aaa\\abc.txt","a") as f :
    while True :
        line = input("글을 입력하세요")
        if line !="":
            f.writelines(line+"\n")
        else :
            break
print("파일이 저장되었습니다.")

# with open("C:\\aaa\\abc.txt","a") as f :
#     while True :
#         line = input("글을 입력하세요 : ")
#         if line !="":
#             f.writelines(line+"\n")
#         else :
#             break

# print("파일이 저장되었습니다.")



# with open("C:\\aaa\\abc.txt","a") as f :
#     while True :
#         line = input("글을 입력하세요. :")
#         if line != "":
#             f.writelines(line+"\n")
#         else :
#             break
# print("파일이 저장되었습니다.")





# stu = []
# with open("C:\\aaa\\test2.txt","r",encoding="UTF-8") as f:
#     while True :
#         line = f.readline()
#         if line=="": break
#         line = line.strip()
#         arr = line.split(",")
#         for i,v in enumerate(arr) :
#             if 2<=i<=5 :
#                 arr[i] = int(v)
#             elif i==6:
#                 arr[i] = float(v)
#         stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})
# print(stu)


# stu = []
# with open("C:\\aaa\\test2.txt","r",encoding="utf-8") as f:
#     while True :
#         line = f.readline()
#         if line =="": break
#         line = line.strip()
#         arr = line.split(",")
#         for i,v in enumerate(arr) :
#             if 5>=i>=2 :
#                 arr[i] = int(v)
#             elif i==6 :
#                 arr[i] = float(v)
#         stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})
# print(stu)