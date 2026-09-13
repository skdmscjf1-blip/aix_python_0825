class Students () :

    s_list=[]

    def add(self,s) :
        self.s_list.append(s)

    def print(self) :
        print()
        print("[학생성적출력]")
        print("*"*60)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
        print("*"*60)
        for s in self.s_list : 
            print(s)
        print()