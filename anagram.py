s="nagaram"
t="anagram"
hash={}


if len(s) != len(t):
    print(False)
else:
    for i,n in enumerate(s):
        hash[i] = n
    print(hash)
    

    