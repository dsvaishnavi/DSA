dominoes = [[1,2],[3,4],[5,6]]
pairs=0
hash={}
for d in dominoes:
   key=tuple(sorted(d))
   
   if key in hash:
       pairs += hash[key]                       
       hash[key] += 1   
   else:
       hash[key] =1
print(pairs)
      
  