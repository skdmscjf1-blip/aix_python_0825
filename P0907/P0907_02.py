import func 
# import func as fn
# from func import hap,hap2,hap3


# 1. 매개변수X, return X - hap()
func.hap()
print("hap()완료")


# 2. 매개변수 O, return X - hap2()
num1 = int(input("숫자입력3 : "))
num2 = int(input("숫자입력4 : "))
func.hap2(num1,num2)
print("hap2()완료")

# 3. 매개변수 O, return O - hap3()
num1 = int(input("숫자입력5 : "))
num2 = int(input("숫자입력6 : "))
total = func.hap3(num1,num2)
print(total)
print("hap3()완료")

