class Students : 
    slist=[]

    def add(self,s) : 
        self.slist.append(s)
        
    def print(self) : 
        print()
        print("*"*60)
        print("[ 학생성적출력 ]")
        print("*"*60)
        print("번호","이름","국어","영어","수학","합계","평균",sep="\t")
        for s in self.slist:
            print(s)