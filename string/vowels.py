s = "aeiassa"
v = "aeiou"
vowel_hash = {}
non_vowel_hash = {}

for i in s:
    if i in v:
        vowel_hash[i] = vowel_hash.get(i, 0) + 1
    else:
        non_vowel_hash[i] = non_vowel_hash.get(i, 0) + 1

# Find max vowel
if vowel_hash:
    max_vowel = max(vowel_hash, key=vowel_hash.get)
    max_vowel_count = vowel_hash[max_vowel]
    
else:
    max_vowel_count = 0
    

# Find max non-vowel
if non_vowel_hash:
    max_non_vowel = max(non_vowel_hash, key=non_vowel_hash.get)
    max_non_vowel_count = non_vowel_hash[max_non_vowel]
    
else:
    max_non_vowel_count = 0

total = max_vowel_count + max_non_vowel_count
print( total)
