s="()[{}"
dict={"(":")","[":"]", "{":"}"}
stack=[]

for i in s:
    if i in dict:
        stack.append(i)
    elif not stack or dict[stack.pop()] != i:
            print(False)
            break
        
else:
    if not stack:
        print(True)
    else:
        print(False)    
        