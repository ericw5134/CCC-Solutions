A = int(input())
B = int(input())
K = int(input())
T = int(input())

d = abs(B - A)

def f(g):
    return g + abs(d - g * K)

q = d // K
cands = []
for g in (q - 2, q - 1, q, q + 1, q + 2):
    if g >= 0:
        cands.append(f(g))

cands.sort()
best = cands[0]

if T == 1:
    print(best)
else:
    second_f = None
    for v in cands:
        if v > best:
            second_f = v
            break

    second_cycle = best + 2
    if second_f is None:
        print(second_cycle)
    else:
        print(min(second_f, second_cycle))