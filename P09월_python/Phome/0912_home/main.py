from Func import *


# 학생성적 txt 불러오기
stu_read ()

while True : 
    #메인화면
    choice=main_screen ()
    if choice == 1:
        #학생성적 입력
        stu_input ()
    elif choice == 2:
        #학생성적 출력
        stu_output ()
    elif choice ==3 :
        #학생성적 수정
        stu_updata ()

    elif choice == 9 :
        #학생성적 txt 저장
        stu_wri ()
    elif choice == 0 :
        print("프로그램이 종료됩니다.")
        break
            






    