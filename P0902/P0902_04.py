
#함수사용이유 : 긴 구문의 반복적인 명령어를 줄일수 있음
#코드를 간결하게 하기 위해서 함수 사용
def stu_print():
    for s in stu :
        print("{}{}{}{}{}{}{}".format(*s))

stu = [
    [1,"홍길동",100,100,100]
    [2,"유관순",100,100,100]
    [3,"이순신",100,100,100]
]

c_no=1
while True :
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적검색")
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:
        print()
        while True:
            no=c_no
            name = input("이름을 입력하세요(0.이전페이지 이동).")
            if name=="0" : break
            #학생전체 출력
            kor = int(input("국어점수입력 : "))
            eng = int(input("영어점수입력 : "))
            math = int(input("수학점수입력 : "))
            total = kor+eng+math
            avg = total/3
            stu.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
            print(name,"학생 성적이 저장되었습니다.")
            c_no += 1
            print()
        
    elif choice ==2:
        #학생을 출력하는 구문
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        for s in stu : 
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}")
        #학생전체 출력
    else :
        name = input("이름을 입력하세요")



# def cal():
#     num1 = int(input("숫자입력. : "))
#     num2 = int(input("숫자입력. : "))
#     print(num1+num2)
#     print(num1-num2)
#     print(num1*num2)
#     print(num1/num2)

# cal()
# cal()
# cal()

# def fun():
#     print("함수를 호출합니다.")

# fun()
# fun()