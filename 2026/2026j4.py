def pack(x, y):
    return ((x & 0xffffffff) << 32) | (y & 0xffffffff)

tokens = open(0, "rb").read().split()
M = int(tokens[0])

visited = set()
x = 0
y = 0
visited.add(pack(x, y))

ans = 0

for mv in tokens[1:]:
    d = mv[0]
    steps = int(mv[1:])

    if d == ord("N"):
        dx, dy = 0, 1
    elif d == ord("S"):
        dx, dy = 0, -1
    elif d == ord("E"):
        dx, dy = 1, 0
    else:
        dx, dy = -1, 0

    for _ in range(steps):
        x += dx
        y += dy
        k = pack(x, y)
        if k in visited:
            ans += 1
        else:
            visited.add(k)

print(ans)