# ============================================================
# Python 26일차
# 클래스 + 파일 + 객체 리스트 종합
# ============================================================


# Q1.
#
# 다음 데이터가 파일에서 읽혔다고 가정합니다.
#
line = "1,영희,90,80,100\n"
#
# ① strip()으로 \n 제거
# ② split(",")로 나누기
#
# 최종 결과가:
#
# ["1", "영희", "90", "80", "100"]
#
# 이 되도록 작성하세요.
# str = line.strip().split(",")


# print(str)



# ============================================================


# Q2.
#
# 아래 Student 클래스가 있습니다.


class Student:

    def __init__(self, no, name, kor, eng, math):
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math


# 아래 data를 이용해서
# Student 객체 s1을 만드세요.
#
# 숫자는 int로 변환하세요.


data = ["1", "영희", "90", "80", "100"]


s1=Student(int(data[0]),(data[1]),int(data[2]),int(data[3]),int(data[4]))

# s1 = ??????




# ============================================================


# Q3.
#
# students 리스트를 만들고
# s1 객체를 append()하세요.
#
#
students = []
#
students.append(s1)




# ============================================================


# Q4.
#
# Student 객체가 여러 개 students 리스트에
# 들어있다고 가정합니다.
#
# for문을 사용해서
# 이름이 "영희"인 학생의
# 국어점수를 95로 변경하세요.
#
#
# 힌트:
#
# for s in students:
#     if ??????:
#         ??????

for i in students :
    if i.name== "영희":
        i.kor = 95




# ============================================================


# Q5.
#
# 다음 Student 클래스에
#
# cal_total()
# cal_avg()
#
# 를 작성하세요.
#
# cal_total()
# → kor + eng + math를
# self.total에 저장
#
# cal_avg()
# → self.total / 3을
# self.avg에 저장


class Student:

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = self.total / 3

    # cal_total 작성
    def cal_total (self) :
        self.total = self.kor + self.eng + self.math
    def cal_avg (self) :
        self.avg = self.total/3

    # cal_avg 작성




# ============================================================


# Q6.
#
# 객체를 파일에 저장하기 위한
# s_str() 함수를 작성하세요.
#
# 결과:
#
# 1,영희,90,80,100
#
# 처럼 문자열로 return되어야 합니다.


class Student:

    def __init__(self, no, name, kor, eng, math):
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    # s_str 작성
    def s_str(self) :
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math}"




# ============================================================


# Q7. 파일 저장
#
# students 리스트 안에
# Student 객체들이 들어있다고 가정합니다.
#
# student.txt 파일에
# 모든 학생정보를 저장하세요.
#
# 조건:
#
# with open()
# "w"
# encoding="utf-8"
# for문
# s.s_str()
# "\n"
#
# 을 사용하세요.

with open("c:/student.txt","w",encoding="utf-8") as f :
    for s in students :
        str = s.s_str()
        f.write(str +"\n")





# ============================================================


# Q8. 종합문제 ⭐
#
# student.txt 파일을 읽어서
#
# ① 한 줄씩 읽기
# ② strip()
# ③ split(",")
# ④ 숫자 int 변환
# ⑤ Student 객체 생성
# ⑥ students 리스트에 append()
#
# 하세요.
#
#
# 파일 데이터 예:
#
# 1,영희,90,80,100
# 2,철수,70,90,80
#
#
# Student 클래스는 이미 있다고 가정하세요.

with open ("student.txt","r",encoding="utf-8") as f :
    while True :
        line = f.readline()
        if line=="":
            break
        data = line.strip().split(",")
        s1=Student(int(data[0]),(data[1]),int(data[2]),int(data[3]),int(data[4]))

        students.append(s1)
        