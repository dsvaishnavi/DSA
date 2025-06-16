apple = [1,3,2]
capacity = [4,3,1,5,2]
applesum=sum(apple)
count=0
sortcapacity=sorted(capacity,reverse=True)
capacitysum=0


for i in sortcapacity:
    capacitysum +=i
    count+=1
    if capacitysum >= applesum:
       break
    
print(count)    
    