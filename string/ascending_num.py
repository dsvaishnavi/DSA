s="1 box has 13 blue 4 red 6 green and 12 yellow marbles"
null=[]
v=s.split()
# m=0
# b=1


for i,j in enumerate (v):
    if j.isdigit():
        null.append(j)
print(len(null))
    
# a=null[0]
# b=a+1
# print(a,b)

# if null[m] <= null[b]:
#     m+=b
#     b+=1
#     print(True)
# else:
#     print(False)
  
  
for b in range(len(null)-1):
    if null[b]>null[b+1]:
        print(False)
        
    else:
        print(True)