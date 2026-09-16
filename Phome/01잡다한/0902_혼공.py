aa = [1,2,3,1,1,1,2,3,1,1,1,2,2,3]
aa_dic = {}

for a in aa :
    if a not in aa_dic :
        aa_dic[a] = 1
    else :
        aa_dic[a] = aa_dic[a]+1
print(aa_dic)
