"""
https://dmoj.ca/problem/ccc20j3
"""

# unzip the input into separate lists of x & y coordinates
xs, ys = [], []
for i in range(int(input())):
    x, y = map(int, input().split(','))
    xs.append(x)
    ys.append(y)

# the smallest x & y coordinates and minus one (because of frame)
print(f'{min(xs)-1},{min(ys)-1}')
# the largest x & y coordinates and plus one (because of frame)
print(f'{max(xs)+1},{max(ys)+1}')