s = "ABAB"
k = 2
start=0
end=0
max_count=0
max_len=0
freq={}

while start < len(s):
    freq[s[start]]=freq.get(s[start],0)+1
    max_count=max(max_count,freq[s[start]])

    if (start - end + 1) - max_count > k :
        freq[s[end]] -= 1
        end+=1
    else:
        max_len=max(max_len,start-end+1)
    start+=1
print(max_len)