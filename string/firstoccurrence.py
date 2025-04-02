haystack = "sabutsad"
needle = "sad"
n= len (needle)

for i in range (len(haystack)):
    f=haystack[i:i+n]
    if f==needle:
        print(i)
        break
else:
    print(-1)

