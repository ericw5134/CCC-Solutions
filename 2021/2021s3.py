'''
https://dmoj.ca/problem/ccc21s3
'''

def get_score(p, f):
    out = 0
    for i in f:
        walk = abs(p - i[0]) - i[2]
        if walk > 0:
            out += walk * i[1]
    return out

n = int(input().strip())

f = []
low = float('inf')
high = 0

for _ in range(n):
    x, y, z = map(int, input().split())
    f.append((x, y, z))
    if x > high:
        high = x
    if x < low:
        low = x

# binary search
while low <= high:
    mid = (low + high) // 2
    s = get_score(mid, f)
    s_left = get_score(mid - 1, f)
    s_right = get_score(mid + 1, f)
    
    if s < s_right and s < s_left:
        break
    if s == s_right or s == s_left:
        break
    if s < s_right:
        high = mid - 1
    elif s < s_left:
        low = mid + 1

print(s)