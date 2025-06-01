s = "babad"
new_s=""


for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub=s[i:j]
        if sub == sub[::-1]:
            if len(sub)>len(new_s):     #longest so checking length
                new_s=sub
print(new_s)