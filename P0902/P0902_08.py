
from func import * #파일과 함수 연결방법

#함수사용 이유
#1. 중복되는 코드를 재사용
#2. 코드를 간결하게 하기 위해 
#프로그램 시작위치------------------------------->
while True :
    choice = main_print()
    result = ran_number(choice)
    print("결과 : ",result)
