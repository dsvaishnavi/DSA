nums = [-1,0,3,5,9,12]
target = 9
left=0
right=len(nums)-1

while (left <= right):
    mid=(left+right)//2                 #precedence is important
    
    if target == nums[mid]:
        print(mid)
        break
    elif target > nums[mid]:
        left=mid+1
    elif target < nums[mid]:
        right=mid-1
else:
    print(-1)