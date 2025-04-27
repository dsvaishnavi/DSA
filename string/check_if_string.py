s = "iloveleetcode"
words = ["love","leetcode","apples"]
v=""


for i in words:
    v+=i
    if v==s:
        print(True)
        break
       
else:
    print(False)
    