'''
https://dmoj.ca/problem/ccc21s1

note:
1. this is a REALLY easy s1 question, just basic math
2. an int output is NOT required, do not write h*((a + b)//2 in area()
'''

def area(a, b, h):
    return h*((a+b)/2)

N = int(input())
heights = list(map(int, input().split()))
widths = list(map(int, input().split()))

total_area = 0
for i in range(N):
    total_area += area(heights[i], heights[i+1], widths[i])

print(total_area)