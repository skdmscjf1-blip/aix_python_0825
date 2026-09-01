# 1-100사이의 숫자맞추기
# 1. 랜덤번호 1개 생성
# 2. 무한으로 입력받기
# 3. 숫자를 입력받기
# 4. 랜덤번호와 숫자 비교
# 5. 결과출력

import random
ran=random.randint(1,100)

no=0
arr = []

while True :
    no = int(input("1-100사이 숫자를 입력하세요. : "))
    arr.append(no)
    if no==ran :
        print("정답입니다!")
        break
    elif no>ran :
        (print(no,"보다 작은수를 입력하세요."))
    else :
        (print(no,"보다 큰수를 입력하세요"))

print("입력한 모든 리스트 : ",arr )
print("정답 : ",arr[-1])

