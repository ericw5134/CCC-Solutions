# 2/15, no idea how to actually solve this
# in a real contest I would just hardcode the 2/15 and do other questions

n = int(input())
arr = [list(map(int, input().split())) for _ in range(2)]

best = 1

def solve(arr):
    b = 1
    if arr[0][0] + arr[0][1] == arr[1][0] + arr[1][1]:
        b = 2
    if (arr[0][0] + arr[0][1] + arr[1][0]) == arr[1][1] * 3:
        b = 2
    if arr[0][0] + arr[0][1] == arr[1][0] * 2 == arr[1][1] * 2:
        b = 3
    if arr[0][0] == arr[0][1] == arr[1][0] == arr[1][1]:
        b = 4
    return b


for _ in range(4):
    best = max(best, solve(arr))
    arr = list(zip(*arr[::-1]))
print(best)