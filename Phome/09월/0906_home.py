products = [
    {"name":"노트북","price":1200000,"stock":5},
    {"name":"마우스","price":30000,"stock":20},
    {"name":"키보드","price":80000,"stock":10},
    {"name":"모니터","price":350000,"stock":7}
]

sales_history = []


while True:

    print()
    print("[ 판매관리 프로그램 ]")
    print("1. 상품목록")
    print("2. 상품판매")
    print("3. 판매내역")
    print("4. 매출분석")
    print("0. 프로그램 종료")

    choice = int(input("원하는 번호를 입력하세요. >> "))


    # 1. 상품목록
    if choice == 1:

        print("[ 상품목록 ]")

        for i, product in enumerate(products):

            print(
                f"{i+1}. "
                f"{product['name']} / "
                f"{product['price']:,}원 / "
                f"재고 {product['stock']}개"
            )


    # 2. 상품판매
    elif choice == 2:

        print("[ 상품판매 ]")

        for i, product in enumerate(products):

            print(
                f"{i+1}. "
                f"{product['name']} / "
                f"{product['price']:,}원 / "
                f"재고 {product['stock']}개"
            )


        prod = int(input("상품번호 : "))

        ea = int(input("구매수량 : "))


        if ea > products[prod-1]["stock"]:

            print("재고가 부족합니다.")
            continue


        products[prod-1]["stock"] -= ea


        total_price = products[prod-1]["price"] * ea


        print(f"결제금액 : {total_price:,}원")


        sales_history.append({

            "product": products[prod-1]["name"],

            "count": ea,

            "total": total_price

        })


    # 3. 판매내역
    elif choice == 3:

        print("[ 판매내역 ]")


        if len(sales_history) == 0:

            print("판매내역이 없습니다.")


        else:

            for sale in sales_history:

                print(
                    f"{sale['product']} / "
                    f"{sale['count']}개 / "
                    f"{sale['total']:,}원"
                )


    # 4. 매출분석
    elif choice == 4:

        print("[ 매출분석 ]")


        if len(sales_history) == 0:

            print("판매내역이 없습니다.")


        else:

            total_sales = 0


            for sale in sales_history:

                total_sales += sale["total"]


            print(f"전체 매출 : {total_sales:,}원")


    # 0. 종료
    elif choice == 0:

        print("프로그램을 종료합니다.")

        break


    else:

        print("잘못된 번호입니다.")