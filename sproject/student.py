class Student :
    def __init__(self,no,name,kor,eng,math) :
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3

        
    def __str__(self) :
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}"

class Students :
    slist = []
    def __init__(self,s) :
        self.slist.append(s)
    

    def add(self,s) :
        self.slist.append(s)


stus = Students(Student(1,"홍길동",100,100,100))
stus.add(Student(2,"유관순",100,100,100))

for ss in stus.slist :
    print(ss)