"""
https://dmoj.ca/problem/ccc18j2

note:
1. try print(zip(list(input()), list(input())) to see what zip() does
"""

days = input()
count = 0
for yesterday, today in zip(list(input()), list(input())):
    if yesterday == 'C' and today == 'C':   # add to count if the spot was occupied both days
        count += 1
print(count)

