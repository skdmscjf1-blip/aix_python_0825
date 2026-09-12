from stuFunc import  *

stu_read()
while True : 
    choice=main_screen()
    if choice == 1:
        stu_input()

    elif choice ==2:
        stu_output()

    elif choice ==3:
        stu_updata ()

    elif choice ==9 :
        stu_write ()

    else :
        print("프로그램이 종료됩니다.")
        break




                

    
