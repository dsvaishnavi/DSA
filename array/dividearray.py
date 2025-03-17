nums=[15,1,4,8,12,11,4,10,4,10,10,15,20,7]
freq={}


for num in nums:
    if num in freq:
        freq[num] +=1
    else:
        freq[num]=1



for i in freq.values():
    if i % 2 != 0:
        print(False)
        break
else:
    print(True)



