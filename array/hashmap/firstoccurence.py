s="leetcode"
hashmap={}
for i in s:
    hashmap[i] = hashmap.get(i, 0) + 1
for i,n in enumerate(s):
    if hashmap[n]==1:
        print(i)
    else:
        print(-1)   
        