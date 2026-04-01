"""
https://dmoj.ca/problem/ccc20j2

note:
1. know what a geometric sequence is: a_N = a_1 * R^{N-1}
"""

P = int(input())
N = people = int(input())
R = int(input())
day = 1
while people <= P:
    # the amount of infections grow in a geometric sequence
    people += N * R ** day
    day += 1

print(day-1)    # we would be 1 day ahead by the end of the while loop