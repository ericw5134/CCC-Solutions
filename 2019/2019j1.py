"""
https://dmoj.ca/problem/ccc19j1
"""

# sum of points for apple
a = 0
for i in range(3, 0, -1):
    a += i * int(input())

# sum of points for banana
b = 0
for i in range(3, 0, -1):
    b += i * int(input())

if a > b:
    print("A")

if b > a:
    print("B")

if b == a:
    print("T")