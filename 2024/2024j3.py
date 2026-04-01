'''
https://dmoj.ca/problem/ccc24j3
'''

import sys

input = sys.stdin.readline  # fast input

n = int(input())
scores = [int(input()) for _ in range(n)]
unique = sorted(set(scores))  # sort scores increasing order and remove duplicates

print(unique[-3], scores.count(unique[-3])) # get third-highest score and the number of times it appears
