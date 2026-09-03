#변수 선언부분 
#개인정보
my_info = {"id":"aaa","pw":"1111",\
           "money":10_000_000,"bonusPoint":0}
#구매리스트
cart = []
# 상품
product = [
    {"p_name":"컴퓨터","price":1000000,"bonusPoint":1000000*0.1},
    {"p_name":"냉장고","price":2000000,"bonusPoint":2000000*0.1},
    {"p_name":"오디오","price":500000,"bonusPoint":500000*0.1},
]
#로그인 부분
while True :
    id = input("아이디 : ")
    pw = input("패스워드 : ")
    if id=="aaa" and pw=="1111" :
        print("로그인 되었습니다.")
        break
    else :
        print("아이디,패스워드가 일치하지 않습니다.")
#구매정보
    print("[ 신나는 쇼핑몰 구매 ]")
    for i,v in enumerate(product) :
        print(f"{i+1}. {v["p_name"]} : {v["price"]}원")
        print("-"*40)
        choice=int(input("원하는 번호를 입력하세요."))

        if choice==1:
            no = int(input("컴퓨터를 구매하시겠습니까?(구매:1,취소:0)"))
            if no==1 :
                print("컴퓨터 구매 완료")
                my_info["money"] -= product[0]["price"] 
                my_info["bonuspoint"] += product[0]["bonuspoint"]
                print(f"나의 돈 : {my_info["money"]:,}원")
                print(f"나의 포인트 : {my_info["bonuspoint"]:,}포인트")

            else :
                print("이전화면으로 이동합니다.")
        elif choice==2:
            no = int(input("컴퓨터를 구매하시겠습니까?(구매:1,취소:0)"))
            if no==1 :
                print("컴퓨터 구매 완료")
                my_info["money"] -= product[0]["price"] 
                my_info["bonuspoint"] += product[0]["bonuspoint"]
                print(f"나의 돈 : {my_info["money"]:,}원")
                print(f"나의 포인트 : {my_info["bonuspoint"]:,}포인트")