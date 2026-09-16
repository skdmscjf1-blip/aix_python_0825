# ============================================================
# 학생성적 프로그램 - 4개 파일 통합 공부용 버전
#
# 원래 파일 구성:
# 1) student.py   → 학생 1명의 정보를 담당
# 2) students.py  → 여러 학생을 리스트로 관리
# 3) stuFunc.py   → 입력, 출력, 수정, 파일읽기/저장 기능
# 4) main.py      → 프로그램 실행
#
# 이 파일은 위 4개 파일을 하나로 합친 버전입니다.
# ============================================================


# ============================================================
# [1] student.py 부분
# 학생 "한 명"의 정보를 만드는 클래스
# ============================================================

class Student:                              # Student = 학생 1명을 만들기 위한 설계도

    def __init__(self, *args):              # Student 객체를 만들 때 자동으로 실행되는 함수
                                             # *args = 여러 개의 값을 한꺼번에 받겠다는 뜻

        if len(args) == 5:                  # 받은 값이 5개라면 → 새 학생을 직접 입력한 경우
            self.no = args[0]               # 0번째 값 = 학생 번호
            self.name = args[1]             # 1번째 값 = 학생 이름
            self.kor = args[2]              # 2번째 값 = 국어 점수
            self.eng = args[3]              # 3번째 값 = 영어 점수
            self.math = args[4]             # 4번째 값 = 수학 점수

            self.total = self.kor + self.eng + self.math
                                             # 국어 + 영어 + 수학 = 총점

            self.avg = self.total / 3        # 총점을 3으로 나눠 평균 계산
            self.rank = 0                    # 처음에는 등수를 모르므로 0으로 저장

        elif len(args) == 8:                 # 받은 값이 8개라면 → 파일에서 학생 정보를 읽은 경우
            self.no = args[0]                # 학생 번호
            self.name = args[1]              # 학생 이름
            self.kor = args[2]               # 국어 점수
            self.eng = args[3]               # 영어 점수
            self.math = args[4]              # 수학 점수
            self.total = args[5]             # 총점
            self.avg = args[6]               # 평균
            self.rank = args[7]              # 등수

    def __str__(self):                       # print(학생객체) 했을 때 자동으로 실행되는 함수
        return (
            f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t"
            f"{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"
        )
                                             # \t = 탭 간격
                                             # :.2f = 소수점 둘째 자리까지 표시

    def s_total(self):                       # 총점을 다시 계산하는 함수
        self.total = self.kor + self.eng + self.math

    def s_avg(self):                         # 평균을 다시 계산하는 함수
        self.avg = self.total / 3

    def s_str(self):                         # 파일에 저장하기 좋은 문자열로 만드는 함수
        return (
            f"{self.no},{self.name},{self.kor},{self.eng},{self.math},"
            f"{self.total},{self.avg:.2f},{self.rank}"
        )
                                             # 쉼표(,)로 각 정보를 연결해서 문자열로 반환


# ============================================================
# [2] students.py 부분
# 여러 학생을 한 곳에 모아서 관리하는 클래스
# ============================================================

class Students:                              # 여러 학생을 관리하는 설계도
    slist = []                               # 학생들을 저장할 리스트
                                             # slist = student list라고 생각하면 쉬움

    def add(self, s):                        # 학생 1명을 추가하는 함수
        self.slist.append(s)                 # slist의 맨 뒤에 학생 s를 추가

    def print(self):                         # 학생 전체를 출력하는 함수
        print()                              # 빈 줄 출력
        print(" " * 25, end="")              # 공백 25칸 출력, 줄바꿈은 하지 않음
        print("[ 학생성적출력 ]")
        print("*" * 60)                      # 별표 60개 출력

        print(
            "번호", "이름", "국어", "영어",
            "수학", "합계", "평균", "등수",
            sep="\t"
        )
                                             # sep="\t" = 각 항목 사이를 탭으로 띄움

        print("*" * 60)

        for s in self.slist:                 # 학생 리스트에서 학생을 한 명씩 꺼냄
            print(s)                         # 학생 1명 출력
                                             # 이때 Student의 __str__()가 자동 실행됨


# ============================================================
# [3] stuFunc.py 부분
# 실제 프로그램 기능을 담당
# ============================================================

stus = Students()                            # Students 객체를 실제로 하나 생성
                                             # 앞으로 stus가 모든 학생을 관리함

stuNum = 1                                  # 새 학생에게 줄 번호
                                             # 처음 학생은 1번부터 시작


# ------------------------------------------------------------
# 학생성적 파일 불러오기
# ------------------------------------------------------------

def readStu():
    global stuNum                           # 함수 밖에 있는 stuNum을 수정하려고 사용

    with open("c:/aaa/stu.txt", "r", encoding="utf-8") as f:
                                             # stu.txt 파일을 읽기 모드(r)로 열기
                                             # f = 열린 파일을 다룰 이름

        while True:                          # 계속 반복
            line = f.readline()              # 파일에서 한 줄 읽기

            if line == "":                   # 더 이상 읽을 내용이 없다면
                break                        # 반복문 종료

            stu = line.split(",")            # 쉼표를 기준으로 문자열 자르기
                                             # 예:
                                             # "1,홍길동,100,90"
                                             # → ["1", "홍길동", "100", "90"]

            for i, s in enumerate(stu):      # 리스트의 번호(i)와 값(s)을 함께 꺼냄

                if 0 <= i <= 1:              # 0번(번호), 1번(이름)은 그대로 둠
                    continue

                elif 2 <= i <= 5:            # 국어~총점은 정수로 변경
                    stu[i] = int(s.strip())   # strip() = 앞뒤 공백과 줄바꿈 제거

                elif i == 6:                 # 평균은 소수이므로
                    stu[i] = float(s.strip()) # float으로 변경

                elif i == 7:                 # 등수는 정수이므로
                    stu[i] = int(s.strip())   # int로 변경

            stus.add(
                Student(
                    stu[0], stu[1], stu[2], stu[3],
                    stu[4], stu[5], stu[6], stu[7]
                )
            )
                                             # Student 객체 1명을 만든 후
                                             # stus의 학생 리스트에 추가

            stuNum = len(stus.slist) + 1     # 현재 학생 수 + 1을 다음 학생 번호로 사용


# ------------------------------------------------------------
# 학생성적 파일 저장하기
# ------------------------------------------------------------

def writeStu():
    with open("c:/aaa/stu.txt", "w", encoding="utf-8") as f:
                                             # stu.txt 파일을 쓰기 모드(w)로 열기

        for s in stus.slist:                 # 모든 학생을 한 명씩 꺼냄
            line = s.s_str()                 # 학생 객체를 파일 저장용 문자열로 변경
            f.write(line + "\n")             # 파일에 한 줄씩 저장
                                             # \n = 다음 줄로 이동

        print("성적파일이 저장되었습니다.")
        print()


# ------------------------------------------------------------
# 0. 메인 화면 함수
# ------------------------------------------------------------

def main_screen():
    print("[ 학생성적프로그램 ]")
    print("1. 성적입력")
    print("2. 성적출력")
    print("3. 성적수정")
    print("9. 성적파일저장")
    print("0. 프로그램종료")
    print("-" * 60)

    choice = int(input("원하는 번호 입력 : "))
                                             # input()은 문자로 입력되므로 int()로 숫자로 변경

    return choice                            # 사용자가 입력한 번호를 함수 밖으로 돌려줌


# ------------------------------------------------------------
# 1. 학생 성적 입력
# ------------------------------------------------------------

def stu_input():
    global stuNum                           # 함수 밖의 stuNum을 사용하고 수정

    while True:                             # 계속 학생을 입력할 수 있도록 반복
        print()
        print("[ 학생성적입력 ]")

        no = stuNum                         # 현재 stuNum을 학생 번호로 사용

        name = input(
            f"{stuNum}번째. 학생이름(0.이전페이지 이동) : "
        )

        if name == "0":                     # 이름 대신 0을 입력하면
            break                           # 학생 입력 화면 종료

        kor = int(input("국어 : "))          # 국어 점수 입력
        eng = int(input("영어 : "))          # 영어 점수 입력
        math = int(input("수학 : "))         # 수학 점수 입력

        total = kor + eng + math            # 총점 계산
        avg = total / 3                     # 평균 계산
        rank = 0                            # 등수는 처음에는 0

        stus.add(Student(no, name, kor, eng, math))
                                             # Student 객체 1명을 만든 뒤
                                             # Students의 slist에 추가

        print(f"{stuNum}.{name} 학생성적이 저장되었습니다.")
        print()

        stuNum += 1                         # 학생 번호를 1 증가
                                             # 1 → 2 → 3 → 4 ...


# ------------------------------------------------------------
# 2. 학생 성적 출력
# ------------------------------------------------------------

def stu_output():
    stus.print()                             # Students 클래스의 print() 함수 실행


# ------------------------------------------------------------
# 3. 학생 성적 수정
# ------------------------------------------------------------

def stu_update():
    print()
    print("[학생성적수정]")

    name = input("학생이름 검색 : ")         # 수정할 학생 이름 입력

    temp = 0                                 # 학생을 찾았는지 확인하는 변수
                                             # 0 = 아직 못 찾음
                                             # 1 = 찾음

    for s in stus.slist:                    # 학생 리스트에서 한 명씩 꺼냄

        if s.name == name:                  # 꺼낸 학생 이름과 검색 이름이 같다면
            temp = 1                        # 학생을 찾았다고 표시

            print(f"{name}학생이 검색되었습니다.")
            print("[ 수정과목 ]")
            print("1. 국어  2. 영어  3. 수학")
            print("*" * 60)

            choice = int(input("과목을 선택하세요.(0.취소)>>"))

            if choice == 0:                 # 0이면 수정 취소
                break

            elif choice == 1:               # 1번 = 국어 수정
                print(" 국어점수 변경 ")
                print("현재점수 : ", s.kor)
                s.kor = int(input("변경점수 입력 : "))

            elif choice == 2:               # 2번 = 영어 수정
                print(" 영어점수 변경 ")
                print("현재점수 : ", s.eng)
                s.eng = int(input("변경점수 입력 : "))

            elif choice == 3:               # 3번 = 수학 수정
                print(" 수학점수 변경 ")
                print("현재점수 : ", s.math)
                s.math = int(input("변경점수 입력 : "))

            s.s_total()                     # 점수가 바뀌었으므로 총점 다시 계산
            s.s_avg()                       # 평균도 다시 계산

            print("수정이 완료되었습니다.")
            print()

    if temp == 0:                           # 끝까지 찾았는데 temp가 0이면
        print(f"{name}학생이 없습니다. 다시 검색하세요.")


# ============================================================
# [4] main.py 부분
# 프로그램을 실제로 시작하는 부분
# ============================================================

readStu()                                   # 프로그램 시작 시 저장된 학생 파일 불러오기

while True:                                 # 사용자가 종료할 때까지 계속 반복

    choice = main_screen()                  # 메인 화면 출력 후 번호 입력받기

    if choice == 1:
        stu_input()                         # 1번 → 학생성적 입력

    elif choice == 2:
        stu_output()                        # 2번 → 학생성적 출력

    elif choice == 3:
        stu_update()                        # 3번 → 학생성적 수정

    elif choice == 8:
        print("[ 등수처리 ]")               # 현재는 제목만 있고 실제 기능은 아직 없음

    elif choice == 9:
        writeStu()                          # 9번 → 학생정보를 파일에 저장

    else:
        print("프로그램 종료")
        break                               # while True 종료 → 프로그램 종료
