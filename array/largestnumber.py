nums = [10,2]
null=""

for i in nums:
    i=str(i)
    null+=i

p=len(null)-1

for i in null:
    if i < p:
        null[i],null[p]=null[p],null[i]
    print(True)


    

    
