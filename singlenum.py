nums=[2,2,1,1,3]
a=[]

for num in nums:
    if num in a:
        a.remove(num)
    else:
        a.append(num)
print(a[0])
        
        
        
 