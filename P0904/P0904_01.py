title = ['번호','이름','국어','영어','수학','합계','평균']
k_title = ['no','name','kor','eng','math','total','avg']
stu = []
cno = 1
def mainPrint () :
    print("[학생성적프로그램]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    choice = int(input("원하는 숫자를 입력하세요 . "))
    return choice

def stuinput () :
    global cno
    while True : 
        print("[ 학생성적입력 ]")
        no = cno
        name = input(f"{no}. 학생이름입력 (0입력 시 뒤로가기): ")
        if name == "0" : break
        kor = int(input("국어점수 :"))
        eng = int(input("영어점수 :"))
        math = int(input("수학점수 :"))
        total = kor+eng+math
        avg = total / 3

        stu.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg})
        print(f"{name}학생성적이 저장되었습니다.")
        cno = cno+1

#메인화면부분
while True :
    choice = mainPrint ()
    if choice == 1: #학생성적 입력
        stuinput ()
            
    elif choice ==2 :
            print("[학생성적출력]")
            print("-"*60)
            print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
            print("-"*60)
            for s in stu :
                print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
    elif choice ==3 :
        print("[학생성적수정]")
        name = input("찾으려는 학생을 입력하세요: ")
        temp = 0
        for i,s in enumerate(stu) :
            if s['name'] == name :
                print(f"{name} 학생을 찾았습니다")
                temp = 1
                break
        if temp == 0:
             print("학생이 없습니다")
        elif temp ==1:
             print("[과목수정선택]")
             print("1.국어  2.영어  3.수학")
             choice = int(input("원하는 번호입력 : "))
             print(f"현재{title[choice+1]} 점수 :{s[k_title[choice+1]]} ")
             s[k_title[choice+1]] = int(input(f"변경하려는 {title[choice+1]}점수"))
             s['total'] = s['kor']+s['eng']+s['math']
             s['avg'] = s['total'] / 3
             print(f"{s['kor']}점으로 {title[choice+1]}점수가 변경되었습니다")
    elif choice ==4 :
             while True :
                print("[성적삭제]")
                can = int(input("삭제할 번호를 입력하시오"))
                del stu[can-1]
                
                break


#a=[1,2,3,4]
# del a[1]
# print(a)

        
            
        
