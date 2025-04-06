s="A man, a plan, a canal: Panama"
s=s.lower()
null=""

for i in s:
    if i.isalnum():
        null +=i

null2=null[::-1]
print(null2)
if null != null2:
    print(False)
else:
    print(True)

# cleaned=null
# null=list(null)

# i=0
# j=len(null)-1

# while i < j:
#     null[i],null[j] = null[j],null[i]
#     i +=1
#     j -= 1
# result=""
# for char in null:
#     result+=char
    
# if result==cleaned:
#     print(True)
# else:
#     print(False)

