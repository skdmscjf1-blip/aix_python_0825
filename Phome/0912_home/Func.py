from student import Student
from students import Students

stus = Students()

stuNum = 1

# 학생성적 txt 불러오기 함수
def stu_read ():
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f : 
        global stuNum
        while True : 
            line = f.readline()
            if line == "": break
            s_str = line.split(",")
            for i,v in enumerate(s_str) :
                if 0<=i<=1 : continue
                elif 2<=i<=5 : s_str[i] = int(v.strip())
                elif i==6 : s_str[i] = float(v.strip())
            stus.add(Student(s_str[0],s_str[1],s_str[2],s_str[3],s_str[4],s_str[5],s_str[6]))
            stuNum = len(stus.s_list)+1

#메인화면 함수
def main_screen () :
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("9. 학생성적저장")
    print("0. 프로그램종료")

    choice = int(input("번호를 입력하세요. : "))
    return choice
#학생성적 입력함수
def stu_input () :
    global stuNum
    while True :
        print()
        print("[학생성적입력]")
        print()
        no=stuNum
        name = input(f"{no}.번째학생 이름입력 (0.이전페이지) : ")
        if name == "0" : break
        kor = int(input("국어점수 : "))
        eng = int(input("영어점수 : "))
        math = int(input("수학점수 : "))
        total = kor+eng+math
        avg = total / 3
        stus.add(Student(no,name,kor,eng,math))
        print(f"{no}번째 {name}학생 성적입력 완료.")
        stuNum += 1
#학생성적 출력 함수
def stu_output ():
    stus.print()

#학생성적 수정함수()
def stu_updata ():
    while True : 
        print()
        print("[학생성적수정]")
        temp = 0
        stu_up = input("성적수정 학생이름 입력 (0.이전페이지) : ")
        if stu_up == "0" : break
        for s in stus.s_list :
            if s.name == stu_up :
                temp=1
                print(f"{stu_up}학생을 찾았습니다")
                print("1.국어  2.영어  3.수학  ")
                a=int(input("수정할 과목을 선택하세요."))
                if a==1 :
                    print(f"현재 국어점수 : {s.kor}")
                    b = int(input("변경할 점수 입력 : "))
                    s.kor = b

                elif a==2 :
                    print(f"현재 영어점수 : {s.eng}")
                    b = int(input("변경할 점수 입력 : "))
                    s.eng = b
                elif a==3 :
                    print(f"현재 수학점수 : {s.math}")
                    b = int(input("변경할 점수 입력 : "))
                    s.math = b
                else : 
                    print("잘못된 번호입니다.")
                    continue

                s.s_total()
                s.s_avg()
                print(f"번호 {s.no}. {stu_up}학생 성적수정 완료")
                break
        if temp == 0 :
            print(f"{stu_up}학생이 없습니다. 다시 입력하세요")

#학생성적 저장 함수()
def stu_wri () :
    print("[학생성적저장]")
    with open("c:/aaa/stu.txt","w",encoding="utf-8") as f:
        for s in stus.s_list :
            wri = s.s_str()
            f.write(wri+"\n")
        print("학생성적이 저장되었습니다.")
