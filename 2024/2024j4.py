'''
https://dmoj.ca/problem/ccc24j4

Note:
1. result of the silly key does not appear in the original string s
2. use a 2-pointer approach to iterate through original string s and wrong string t
'''

s = input() + "."  # original string
t = input() + "."  # wrong(?) string

quiet = '-'
silly = ['-', '-']  # [original character, wrong character]

for c in "qwertyuiopasdfghjklzxcvbnm":  # find the wrong character
    if c in t and c not in s:
        silly[1] = c

i = j = 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:  # same letter, we can just continue
        i += 1
        j += 1
        continue

    if t[j] == silly[1]:  # if t[j] is silly key, then s[i] must be the original character! 
        silly[0] = s[i]
        i += 1
        j += 1
        
    else:  # if t[j] is not the silly key AND s[i] != t[j], then it must be the quiet key
        quiet = s[i]
        i += 1  # only increment i since the quiet key doesn't result in any characters being typed

print(*silly)
print(quiet)