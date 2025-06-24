nums = [3,4,9,1,3,9,5]
key = 9
k = 1
null=[]

indices= [i for i, val in enumerate(nums) if val == key]

for i in range(len(nums)):
    for j in indices:
        if abs(i-j)<=k and nums[j]==key:
            null.append(i)
            break
print(null)
            