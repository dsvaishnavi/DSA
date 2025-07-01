nums = [1,1,1]
k = 2
# Output: 2
sum=0
prefix_count={0:1}
count=0

for i in nums:
    sum+=i
    count+=prefix_count.get(sum-k,0)
    prefix_count[sum]=prefix_count.get(sum,0)+1
print(count)