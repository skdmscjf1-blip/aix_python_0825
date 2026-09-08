class Student :
    def __init__(self,no,name,kor,eng,math) :
        self.__no = no
        self.__name = name
        self.__kor = kor # __ 캡슐화 : 클래스 내부에서만 값을 수정
        self.__eng = eng
        self.__math = math
        self.__total = kor + eng + math
        self.__avg = (kor+eng+math) / 3
    def __str__(self) :
        return f"{self.__no}\t{self.__name}\t{self.__kor}\t{self.__eng}\t{self.__math}\t{self.__total}\t{self.__avg:.2f}"

    def get_kor(self) :
        return self.__kor

    def set_kor(self,kor) :
        self.__kor = kor

    def sum(self) :
        self.__sum = self.__kor+self.__eng+self.__math
    def avg(self) :
        self.__avg = self.__sum / 3

    def print(self) :
        print(self.__no,self.__name,self.__kor,self.__eng,self.__math,self.__total,f"{self.__avg:.2f}",sep ="\t")

s = Student(1,"홍길동",100,100,99)

print("*"*50)
print(s)
print("*"*50)
s.kor = 70 #클래스 변수값 수정
s.math = 40 #클래스 변수값 수정
s.set_kor(50)
s.print()
print(s)