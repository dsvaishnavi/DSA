s="1 box has 13 blue 4 red 6 green and 12 yellow marbles"
null=[]

v=s.split()

for i,j in enumerate (v):
    if j.isdigit():
        null.append(int(j))
print(null)
    

flag = True
for b in range(len(null)-1):
    if null[b]>null[b+1]:
        flag=False
        break
print(flag)