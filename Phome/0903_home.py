
def total2() :
    print()
    print("[ 학생성적출력 ]")
    print("-"*60)
    print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
    print("-"*60)
    for s in stu:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
    print()

def total() :
    count_no = 1
    print()
    while True :
        print("[학생성적입력]")
        no = count_no
        name = input("학생이름입력 (0.이전페이지 이동) : ")
        if name == "0": break
        kor = int(input("국어점수입력 : "))
        eng = int(input("영어점수입력 : "))
        math = int(input("수학점수입력 : "))
        total = kor+eng+math
        avg = total/3
        stu.append(
            {"no":no,"name":name,"kor":kor,"eng":eng,\
            "math":math,"total":total,"avg":avg})
        print(name,"학생성적이 저장되었습니다.")
        count_no = count_no+1
    print()
    

# 학생성적
stu = [
    # {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100},
    # {},
    # {}
]
# 화면출력
# 1. 성적입력
# 2. 성적출력

while True : 
    print("[학생성적프로그램]")
    print("-"*60)
    print("1. 학생성적입력")
    print("1. 학생성적출력")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요."))
    # 학생성적입력부분
    if choice == 1:
        total()
    # 학생성적출력부분
    elif choice ==2:
        total2()


# my_info = {"id":"aaa","pw":"1111",\
#         "name":"홍길동","money":10_000_000}
# s_arr = [
#     {"prd_name":"컴퓨터","price":1000000},
#     {"prd_name":"냉장고","price":2000000},
#     {"prd_name":"오디오","price":500000},
#     {"prd_name":"세탁기","price":1500000}
#     ]

# def p_cal(choice) :
#     if my_info['money'] < s_arr[choice-1]['price']:
#         print("잔액이 부족합니다. 잔액을 충전하세요.")
#         return 
#     print(f"구매상품 : {s_arr[choice-1]['prd_name']}")
#     print(f"가격 : {s_arr[choice-1]['price']:,}원")
#     my_info['money'] =my_info['money']-s_arr[choice-1]['price']
#     print(f"상품구매 후 잔액 : {my_info['money']:,}원")

# while True :
#     for i,v in enumerate(s_arr) :
#         print(f"{i+1}. {v['prd_name']}: {v['price']}원")

#     choice = int(input("원하는 번호를 입력하세요.>>>"))
#     if choice==1:
#         p_cal(choice)
#     elif choice==2:
#         p_cal(choice)
#     elif choice==3:
#         p_cal(choice)
#     elif choice==4:
#         p_cal(choice)




# # 앞에숫자에는 10곱하고, 뒤에 숫자에는 100 곱해서
# # # 합계를 구하시오.
# # # 1*10+3*100 = 310
# num = input("숫자입력(1/3)")
# num2 = num.split("/")
# alist = [int(i) for i in num2]
# print("{}+{}={}".format((alist[0])*10,(alist[1])*100,(((alist[0])*10))+((alist[1])*100)))

# def cal(n1,n2) :
#     r1 = n1+n2
#     r2 = n1-n2
#     r3 = n1*n2
#     r4 = n1/n2
#     return r1,r2,r3,r4

# n1 = int(input("숫자입력 : "))
# n2 = int(input("숫자입력 : "))
# r1,r2,r3,r4=cal(n1,n2)
# print(r1,r2,r3,r4)


