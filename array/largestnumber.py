nums = [10,2]
null=""
null2=""
for i in nums:
    i=str(i)
    null+=i


new=list(null)

leng=len(new)

for i in range(leng):
    for j in range(0,leng-i-1):
        if new[j] < new[j+1]:
            new[j],new[j+1]=new[j+1],new[j]



for p in new:
    null2+=p
print(null2)
    
            
    

    
