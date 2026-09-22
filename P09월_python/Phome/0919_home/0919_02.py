# # ============================================================
# # Python 24일차
# # 캡슐화 / getter / setter
# # ============================================================


# # Q1.
# #
# # 다음 중 __kor를 사용하는 가장 큰 이유는?
# #
# # ① 반복문을 실행하려고
# # ② 값을 외부에서 함부로 직접 수정하지 않도록 관리하려고
# # ③ 파일을 읽으려고
# # ④ 리스트를 만들려고
# #
# # 정답: 2번


# # ============================================================


# # Q2.
# #
# # 다음 코드에서
# #
# # self.__kor
# #
# # 와
# #
# # kor
# #
# # 의 차이를 설명하세요.
# #
# #
# # def set_kor(self, kor):
# #     self.__kor = kor
# #
# #
# # self.__kor = 보호되고있는 값
# #
# # kor = 보호되고있는 값을 변경하기위한 값


# # ============================================================


# # Q3.
# #
# # 다음 Student 클래스에
# # get_kor()를 작성하세요.
# #
# # get_kor()는 __kor 값을 return해야 합니다.


# # class Student:

# #     def __init__(self, kor):
# #         self.__kor = kor

# #     # get_kor 작성

# #     def get_kor(self):
# #         return self.__kor

  


# # ============================================================


# # Q4.
# #
# # 다음 Student 클래스에
# # set_kor()를 작성하세요.
# #
# # 새로운 국어점수가
# # 0~100이면 저장하고
# #
# # 그 외에는:
# #
# # "잘못된 점수입니다."
# #
# # 를 출력하세요.


# # class Student:

# #     def __init__(self, kor):
# #         self.__kor = kor

# #     def get_kor(self):
# #         return self.__kor

# #     # set_kor 작성
# #     def set_kor(self,kor):
# #         if 0<=kor<=100 :
# #             self.__kor=kor
# #         else : 
# #             print("잘못된 점수입니다.")



# # ============================================================


# # Q5.
# #
# # 아래 코드를 보고 출력 결과를 예상하세요.


# # class Student:

# #     def __init__(self, kor):
# #         self.__kor = kor

# #     def get_kor(self):
# #         return self.__kor


# # s1 = Student(90)

# # s1.kor = 50

# # print(s1.get_kor())


# # 출력 결과: 처음 객체에 90을 넣엇음. 그다음 50을 넣으려고 했으나 __kor 형태로 보호받고있어서 50으로 변경안되고 90으로 출력됨
# #
# # 왜 그런지도 설명하세요.


# # ============================================================
# # Q6. 실무 응용
# # ============================================================
# #
# # 회원권 잔여횟수를 관리하는 클래스를 만드세요.
# #
# # 클래스 이름:
# # Member
# #
# #
# # 객체를 만들 때
# # remaining을 전달받아
# # self.__remaining에 저장하세요.
# #
# #
# # get_remaining()
# # → 잔여횟수 return
# #
# #
# # set_remaining(value)
# #
# # value가 0 이상이면 저장
# #
# # value가 음수이면:
# #
# # "잔여횟수는 음수가 될 수 없습니다."
# #
# # 출력


class Member:
    def __init__(self,remaining):
        self.__remaining = remaining

    def get_remaining(self):
        return self.__remaining

    def set_remaining(self,value) :
        if value >=0 :
            self.__remaining = value
        else :
            print("잔여횟수는 음수가 될 수 없습니다.")

m1 = Member(50)
print(m1.get_remaining())
(m1.set_remaining(-10))
print(m1.get_remaining())

    