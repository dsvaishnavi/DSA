nums=[0,1,2,2,3,0,4,2]
val=2
               
i = 0  # Pointer to track the position for valid elements
for num in nums:
    if num != val:
        nums[i] = num  # Overwrite nums[i] with valid element
        i += 1  # Move pointer forward

print(i) 
