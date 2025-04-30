sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
s=sentence.split()
print(s)


count=0

for token in s:
    for i in token:
        if  i.isdigit():  #if there is number skip it
            continue
        
    index=token.find("-")
    if index == 0 or index >= len(token)-1:
        continue
         
hash={"!",",","."}  
plus=0

for h in hash:
    if h in token:
        plus+=1
    if plus > 1:
        continue
    
    
    valid = True
    for ch in token:
        if not (ch.islower() or ch == '-' or ch in hash):
            valid = False
            break
    if valid:
        count += 1

print(count)    
    

        
         
         
         
         
         
         
         
         
         
#         sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
# tokens = sentence.split()
# count = 0

# for word in tokens:
#     # Skip if any digit is present
#     if any(ch.isdigit() for ch in word):
#         continue

#     # Check hyphen rules
#     if word.count('-') > 1:
#         continue
#     if '-' in word:
#         idx = word.index('-')
#         if idx == 0 or idx == len(word)-1:
#             continue
#         if not (word[idx-1].islower() and word[idx+1].islower()):
#             continue

#     # Check punctuation rules
#     punc = {'!', '.', ','}
#     punc_count = 0
#     for ch in word:
#         if ch in punc:
#             punc_count += 1

#     if punc_count > 1:
#         continue
#     if punc_count == 1 and word[-1] not in punc:
#         continue

#     # Check all characters are valid
#     valid = True
#     for ch in word:
#         if not (ch.islower() or ch == '-' or ch in punc):
#             valid = False
#             break
#     if valid:
#         count += 1

# print(count)