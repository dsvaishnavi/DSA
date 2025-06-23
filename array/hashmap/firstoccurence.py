s="leetcode"
hashmap={}
for i in range (len(s)):
    if i not in hashmap:
        hashmap.add(i)
    else:
        hashmap.get(i,0)+1
        print(hashmap)