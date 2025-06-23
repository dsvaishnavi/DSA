nums=[1,2,3,4]
prefix = [0] * len(nums)

for i in range(1, len(nums)):
    prefix[i] = prefix[i - 1] + nums[i - 1]

print(prefix) 


n = len(nums)
suffix = [0] * n

for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] + nums[i + 1]

print(suffix)

