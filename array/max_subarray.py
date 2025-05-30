nums= [5,4,-1,7,8]
maxSum=nums[0]
currSum=0

for n in nums:
    currSum+=n
    if currSum > maxSum:
        maxSum=currSum
       
    if currSum < 0:
        currSum=0
print(maxSum)
    
    