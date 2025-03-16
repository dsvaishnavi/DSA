nums=[3,2,4]
target=6
hashmap={}

for i,num in enumerate (nums):
    minus= target-num
    if minus in hashmap:
        print(hashmap[minus],i)
    else:
        hashmap[num]=i
        
   
        


    


    