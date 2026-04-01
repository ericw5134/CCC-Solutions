"""
https://dmoj.ca/problem/ccc22j5
"""

n = int(input())
trees = []
for _ in range(int(input())):
    trees.append(tuple(map(int, input().split())))
trees += [(0, 0), (n + 1, n + 1)]

all_x,  all_y = set(), set()
for x, y in trees:
    for x2, y2 in trees:
        if x != x2:
            all_x.add(tuple(sorted((x, x2))))
        if y != y2:
            all_y.add(tuple(sorted((y, y2))))


def sort_by_abs(cords):
    return list(sorted(cords, key=lambda cord: abs(
        cord[0] - cord[1]), reverse=True))


trees = trees[:-2]
all_x, all_y = sort_by_abs(all_x), sort_by_abs(all_y)

total = []
for i in range(2):
    trees = sorted(trees, key=lambda x: x[i])
    for s, e in all_x if i else all_y:
        s2, e2 = 0, abs(s - e)
        for tree in trees:
            if i and s < tree[0] < e and s2 < tree[1] < e2:
                e2 += abs(tree[1] - s2) + 1
                s2 = tree[1] + 1
            elif not i and s < tree[1] < e and s2 < tree[0] < e2:
                e2 += abs(tree[0] - s2) + 1
                s2 = tree[0] + 1
            if e2 > n + 1:
                break
        else:
            total.append(abs(s - e) - 1)
            break

print(max(total))