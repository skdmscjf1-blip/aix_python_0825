from pfunc import*



stu_read ()     #학생성적 파일불러오기
while True : 
    
    choice=main_moniter()   #메인화면
    if choice == 1: 
        stu_input () #학생성적입력

    elif choice ==2: 
        stu_output () #학생성적출력
    elif choice ==3:
        pass
    elif choice ==9 : 
        stu_wri ()  #성적파일 저장