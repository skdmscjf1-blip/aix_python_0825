stu_list=[]
stuNum = 1


def stu_read() :
    global stuNum
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f :
        while True:
            line = f.readline()
            if line == "": break
            stu = line.split(",")
            for i,v in enumerate(stu) :
                if 0<=i<=1 : continue
                elif 2<=i<=5 : stu[i] = int(v.strip())
                elif i==6 : stu[i] = float(v.strip())
            stu_list.append({"no":stu[0],"name":stu[1],"kor":stu[2],"eng":stu[3],"math":stu[4],"total":stu[5],"avg":stu[6]})
            stuNum = len(stu_list)+1

def stu_write () :
    with open("c:/aaa/stu.txt","w",encoding="utf-8") as f :
        for s in stu_list : 
            s_save = f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']:.2f}"
            f.write(s_save+"\n")
        print("성적이 저장되었습니다.")

def main_screen() :
    
        print("[학생성적프로그램]")
        print("1. 학생성적입력")
        print("2. 학생성적출력")
        print("3. 학생성적수정")
        print("9. 성적파일저장")
        print("0. 프로그램종료")
        print("-"*60)

        choice = int(input("원하는 번호 입력 : "))
        return choice

def stu_input() :
    while True :
        global stuNum
        print()
        print("[학생성적입력]")
        no = stuNum
        name = input(f"{stuNum}번째학생 이름입력 (0.이전페이지): ")
        if name == "0": break
        kor = int(input("국어점수 : "))
        eng = int(input("영어점수 : "))
        math = int(input("수학점수 : "))
        total = kor+eng+math
        avg = total / 3
        stu_list.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg})
        print(f"{stuNum}번째 {name}학생 성적 입력완료되었습니다.")
        stuNum += 1

def stu_output() :
    print()
    print("[학생성적출력]")
    print("-"*60)
    print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
    print("-"*60)
    for s in stu_list :
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")

def stu_updata () :
    print()
    print("[학생성적수정]")
    name = input("수정할 학생이름 입력 : ")
    temp = 0
    for s in stu_list : 
        if name == s["name"] :
            temp = 1
            print(f"{name} 학생을 찾았습니다.")
            print("1국어  2.영어  3.수학")
            a=int(input("수정할 번호 입력 (0.취소) : "))
            if a == 0: break
            if a==1 :
                print("국어점수 변경")
                print(f"현재 국어점수: {s["kor"]}")
                s["kor"] = int(input("변경할점수 입력: "))
                
            elif a==2 :
                print(f"현재 영어점수: {s["eng"]}")
                s["eng"] = int(input("변경할점수 입력: "))
            
            elif a==3 :
                print(f"현재 수학점수: {s["math"]}")
                s["math"] = int(input("변경할점수 입력: "))

        s["total"] = s["kor"] + s["eng"] + s["math"]
        s["avg"] = s["total"] / 3
    print("수정이 완료되었습니다.")
    print()
    if temp==0:
        print(f"{name}학생 없음. 다시 입력하세요")  