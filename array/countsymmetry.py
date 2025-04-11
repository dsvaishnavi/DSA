low=1
high=100

count=0

for num in range(low, high + 1):
    str_num=str(num)
    
    if len(str_num)%2 !=0:
        continue
    
    mid= len(str_num) // 2
    firsthalf=str_num[:mid]
    last=str_num[mid:]
    
    firsthalf=sum(int(d) for d in firsthalf)
    last=sum(int(i)for i in last)
    
    if firsthalf==last:
        count +=1
    print(count)