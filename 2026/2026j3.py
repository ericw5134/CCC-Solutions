def beats(a, b):
    return (a == "R" and b == "G") or (a == "G" and b == "B") or (a == "B" and b == "R")

ngoc = input()
minh = input()

i = 0
j = 0
n = len(ngoc)
m = len(minh)
eaten_ngoc = 0
eaten_minh = 0

while i < n and j < m:
    a = ngoc[i]
    b = minh[j]
    if a == b:
        eaten_ngoc += 1
        eaten_minh += 1
        i += 1
        j += 1
    else:
        if beats(a, b):
            eaten_ngoc += 1
            j += 1
        else:
            eaten_minh += 1
            i += 1

if i < n:
    eaten_ngoc += n - i
if j < m:
    eaten_minh += m - j

print(eaten_ngoc)
print(eaten_minh)