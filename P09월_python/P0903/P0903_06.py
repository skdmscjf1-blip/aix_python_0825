my_info = [
    {"money":10_000_000}
]
s_arr = [
    {"prd_name":"컴퓨터","price":1000000},
    {"prd_name":"냉장고","price":2000000},
    {"prd_name":"오디오","price":500000},
    {"prd_name":"세탁기","price":1500000}
    ] # 1-0,2-1,3-2

def na(choice) :
    if my_info[0]['money'] < s_arr[choice-1]['price'] :
        print("잔액이 부족합니다. 잔액을 충전하세요.")
        return 
    print(f"제품명 : {s_arr[choice-1]['prd_name']}")
    print(f"가격 : {s_arr[choice-1]['price']:,}원 ")
    my_info[0]['money'] = my_info[0]['money']-s_arr[choice-1]['price']   
    print(f" 구매후 잔액 : {my_info[0]['money']:,}")

while True :
    for i,v in enumerate(s_arr):
        print(f"{i+1}. {s_arr[i]['prd_name']}: {s_arr[i]['price']:,}원")
    choice = int(input("원하는 번호입력 : "))
    if choice == 1:
        na(choice)
    elif choice == 2:
        na(choice)
    elif choice == 3:
        na(choice)
    elif choice == 4:
        na(choice)