'''
given a set of numbers size n, determine minimum amount of numbers needed to get to a given distance with repetition allowed.

if there were clubs 2,4,5 and the total distance was 12
then it would take 3 clubs (5, 5 and 2)

method is calculate # for all distances from 0 to given!
F(0) = 0
F(n) = (minimum of F(n-i), where i = given #s and minimum >= 0) + 1

using the above example of 2, 4 and 5 clubs you would have:
F(0) = 0
F(1) = -1, make F(i) = -1 if we can't get there
F(2) = 1
F(3) = -1
F(4) = 1
F(5) = 1
F(6) = 2 because F(6-2) = 1 is min, therefore answer is F(4) + 1 (another 2) = 2
F(7) = 2 because F(7-2) = 1 is min, therefore answer is F(5) + 1 = 2
F(8) = 2 because F(8-4) = 1 is min, therefore answer is F(4) + 1 = 2
F(9) = 2 because F(9-4) = 1 is min, therefore answer is F(5) + 1 = 2
F(10) = 2 because F(10-5) = 1 is min, therefore answer is F(5) + 1 = 2
F(11) = 3 because F(11-2) = 2 is min, therefore answer is F(9) + 1 = 3
F(12) = 3 because F(12-2) = 2 is min, therefore answer is F(10) + 1 = 3
'''

import sys
import math

def solve(distance, clubs):
    INF = 10**9
    F = [-1] * (distance + 1)
    F[0] = 0
    for x in range(1, distance + 1):
        best = INF
        for club in clubs:
            t = x - club
            if t >= 0 and F[t] >= 0 and F[t] < best:
                best = F[t]
        F[x] = best + 1 if best < INF else -1
    return F[distance]


data = sys.stdin.read().strip().split()
it = iter(map(int, data))
distance = next(it)
n = next(it)
clubs = [next(it) for _ in range(n)]
ans = solve(distance, clubs)
if ans == -1:
    print("Roberta acknowledges defeat.")
else:
    print(f"Roberta wins in {ans} strokes.")