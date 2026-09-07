from homefunc import*

stu_read ()
while True : 
    choice = main_screen ()
    if choice ==1:
        stu_input ()
    elif choice ==2:
        stu_output ()
    elif choice == 3:
            pass
    elif choice == 9 :
        stu_save ()
    elif choice == 0 :
        print("프로그램이 종료됩니다.")
        break