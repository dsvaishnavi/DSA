s ="abaccbc"
hash={}

for i in s:
    if i in hash:
        hash[i] +=1
    else:
        hash[i] = 1
val=list(hash.values())
   
same = True
first = val[0]


for v in val:
    if v != first:
        same =False
print(same)
    




