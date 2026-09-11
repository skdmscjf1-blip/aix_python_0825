from stuFunc import  *

with open("c:/aaa/stu.txt","r",encoding="utf-8") as f :
    while True:
        line = f.readline()
        if line == "": break
        stu = line.split(",")
        



    while True : 
        choice=main_screen()
        if choice == 1:
            stu_input()
        elif choice ==2:
            stu_output()
        elif choice ==3:
            stu_updata ()
        elif choice ==0:
            print("프로그램이 종료됩니다.")
            break




                

    
