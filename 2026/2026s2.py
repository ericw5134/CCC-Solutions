from array import array

it = iter(open(0, "rb").read().split())
N = int(next(it))
L = int(next(it))
Q = int(next(it))

diff = array("i", [0]) * (N + 3)

for _ in range(L):
    p = int(next(it))
    s = int(next(it))
    l = p - s
    r = p + s
    if l < 1:
        l = 1
    if r > N:
        r = N

    # we are going to indicate where we start adding 1
    # and subtracting 1, this is the fastest way
    diff[l] += 1
    diff[r + 1] -= 1

# use an accumulator variable to add 1s
run = 0
for i in range(1, N + 1):
    run += diff[i]
    diff[i] = run   # try printing diff & run each iteration and see what this is doing

out = []
for _ in range(Q):
    x = int(next(it))
    out.append("Y" if diff[x] > 0 else "N")

print("\n".join(out))