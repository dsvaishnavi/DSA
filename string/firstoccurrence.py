haystack = "sadbutsad"
needle = "sad"
n= len (needle)
for i,j in enumerate (haystack):
    f=haystack[i:i+n]
    if f==needle:
        print(i)
        break
else:
    print(-1)

