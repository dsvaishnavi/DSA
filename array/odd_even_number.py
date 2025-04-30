nums = [121,345,211,611,7896]
count=0

for i in nums:
    i=str(i)
    l=len(i)
    
    if l % 2 == 0:
        count+=1
        
    else:
        continue
print(count)
        