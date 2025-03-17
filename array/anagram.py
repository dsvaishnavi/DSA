s="cat"
t="nnh"

if len (s) != len (t):
    print(False)
else :
    hash_s={}
    hash_t={}
    
    for i in s:
        hash_s[i] = hash_s.get(i,0)+1
    for i in t:
        hash_t[i]=hash_t.get(i,0)+1
    print(hash_s==hash_t)