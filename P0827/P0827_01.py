
# # 학생 2명의 성적을 입력받아 출력하시오.
# # 번호, 이름, 국어,영어,수학 점수를 입력받아
# # 번호, 이름, 국어,영어,수학,합계,평균을 출력하시오

# #1. 성적입력
# #2. 성적처리 수식
# #3. 성적출력

# no = input("번호를 입력하시오")
# name = input("이름을 입력하시오")
# a = int(input("국어점수를 입력하시오"))
# b = int(input("영어점수를 입력하시오"))
# c = int(input("수학점수를 입력하시오"))
# #2. 성적처리 수식
# total = a+b+c
# avg = total/3

# no2 = input("번호를 입력하시오")
# name2 = input("이름을 입력하시오")
# a2 = int(input("국어점수를 입력하시오"))
# b2 = int(input("영어점수를 입력하시오"))
# c2 = int(input("수학점수를 입력하시오"))

# total2 = a2+b2+c2
# avg2 = total2/3
# #3. 성적출력
# print("*"*70)
# print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
# print("*"*70)
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(no,name,a,b,c,total,avg))
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(no2,name2,a2,b2,c2,total2,avg2))
# print("*"*70)