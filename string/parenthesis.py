s="()[]{}"
dict={"(":")","[":"]", "{":"}"}
stack=[]

for a in s:
    if a in dict:
        stack.append(a)
    elif not stack or dict[stack.pop()]!= a:
        print(False)
        break
else:
    if not stack:
            print(True)
    else:
            print(False)
           
        