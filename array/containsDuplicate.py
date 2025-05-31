nums = [1,2,3,1]
null = set()

for i in nums:
    if i in null:
        print(True)
        break
    null.add(i)
else:
    print(False)