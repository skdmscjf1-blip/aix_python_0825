# pip install selenium
# pip install requests
# pip install beautifulsoup4
# pip install lxml
# jupyter
# 크롬드라이버
#pip install python-dotenv


#1-100까지 랜덤숫자를 1개 생성해서
#무한반복해서 숫자를 맞추는 프로그램을 구현하시오.
#입력한 숫자가 크면 크다
#입력한 숫자가 작으면 작다라고 출력
#맞추면 정답이라고 출력후 프로그램 종료 
import random 

ran_num= random.randint(1,100)
print(ran_num)
arr_num=[]

while True : 
    input_num = int(input("숫자를 입력하세요. : ")) #타입 : str -> int
    arr_num.append(input_num) #입력한 숫자 리스트에 추가
    if input_num == ran_num :
            print("정답")
            break
    elif input_num > ran_num :
            print("입력한 숫자가 더 큽니다.")
    else :
            print("입력한 숫자가 더 작습니다.")

print("랜덤숫자 : ",ran_num)
print("입력한 모든 숫자 : ",arr_num)
