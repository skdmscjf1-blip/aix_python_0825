title = ["번호",'이름','국어','영어','수학','합계','평균']
stu = []
sno = 1 #학생성적인원변수 - db

# 함수선언 ------------------------------------
def s_mainPrint():
    # 메인화면부분
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("-"*60)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    return choice

# 학생성적입력함수선언
def s_input(sno):
    while True: #입력을 멈추고 싶을때까지 입력받음
        no = sno
        print("[ 학생성적입력 ]")
        name = input(f"{no}번째 이름입력 (0.이전화면이동) : ")
        if name == "0": break
        kor = int(input("국어점수입력 : "))
        eng = int(input("영어점수입력 : "))
        math = int(input("수학점수입력 : "))
        total = kor+eng+math
        avg = total/3

        # 리스트저장 - 파일저장 - db저장
        stu.append({'no':no,'name':name,'kor':kor,\
                    'eng':eng,'math':math,'total':total,\
                        'avg':avg})
        print(f"{name} 학생성적이 저장되었습니다.")
        print()
        # score = [0]*3
        # for i in range(3):
        #     score[i] = int(input(f"{title[i+2]} 점수입력 : "))
        sno += 1
    return sno

#----------------------------------------------------
while True:
    choice = s_mainPrint()  # 메인화면부분 함수호출
    if choice == 1: # 학생성적입력부분
        sno = s_input(sno)