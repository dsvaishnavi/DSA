word ="cuaieuouac"
vol=set("aeiou")
count=0

for i in range(len(word)):
    if word[i] in vol:
        seen=set()
        for j in range(i,len(word)):
            if word[j] in vol:
                seen.add(word[j])
                if len(seen)==5:
                    count+=1
            else:
                break
print(count)



    
        



