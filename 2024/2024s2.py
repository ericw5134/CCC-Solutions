'''
https://dmoj.ca/problem/ccc24s2
'''

t, n = map(int, input().split())

words = []
cases = []
for _ in range(t):
    words.append(input())
#print(words)

frequency = [0] * 26    # freq array to count the # of times each letter occured

for word in words:
    heavy = "T"
    case1 = False
    case2 = False

    for i in range(len(word)):
        index = ord(word[i]) - ord('a')
        #print(word[i] + "'s index is: ", index)
        frequency[index] += 1
    #print(frequency)
    
    if frequency[ord(word[0]) - ord('a')] > 1:
        case2 = True 
    else:
        case1 = True
    
    # 12121212 case 1
    if case1:
        for i in range(len(word)):
            if i % 2 != 0 and frequency[ord(word[i]) - ord('a')] < 2:   # odd index
                #print(word[i] + " violated case 1 at index ", i)
                heavy = "F"
            
            if i % 2 == 0 and frequency[ord(word[i]) - ord('a')] != 1:  # even index
                #print(word[i] + " violated case 1 at index ", i)
                heavy = "F"
    
    # 21212121 case 2
    if case2:
        for i in range(len(word)):
            if i % 2 != 0 and frequency[ord(word[i]) - ord('a')] != 1: # odd index
                #print(word[i] + " violated case 2 at index ", i)
                heavy = "F"
            
            if i % 2 == 0 and frequency[ord(word[i]) - ord('a')] < 2:  # even index
                #print(word[i] + " violated case 2 at index ", i)
                heavy = "F"
    
    cases.append(heavy)
    
    frequency = [0] * 26

for case in cases:
    print(case)