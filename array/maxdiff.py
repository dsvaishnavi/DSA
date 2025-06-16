nums = [7,1,4]
maxdiff=-1

for i in range(len(nums)-1):
    for j in range (i+1,len(nums)):
        if nums[j]>nums[i]:
           maxdiff=max(maxdiff,nums[j]-nums[i])
print(maxdiff) 

