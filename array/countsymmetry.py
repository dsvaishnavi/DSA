low=1
high=100
count=0

for num in range(low,high+1):
    str_num=str(num)
    
    if len(str_num)%2 !=0:
        continue
    
    center=len(str_num)//2
    first_half=str_num[:center]
    other_half=str_num[center:]
    
    first_half=sum(int(d) for d in first_half)
    other_half=sum(int(a)for a in other_half)
    
    if first_half==other_half:
        count+=1
    print(count)