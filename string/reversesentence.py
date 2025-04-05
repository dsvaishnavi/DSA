s="race a car"
s=s.lower()
null=""

for i in s:
    if i.isalnum():
        null +=i
print(null)

cleaned=null
null=list(null)

i=0
j=len(null)-1

while i < j:
    null[i],null[j] = null[j],null[i]
    i +=1
    j -= 1
result=""
for char in null:
    result+=char

print(result)
if result==cleaned:
    print(True)
else:
    print(False)

