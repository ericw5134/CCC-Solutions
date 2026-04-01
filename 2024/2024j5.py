'''
https://dmoj.ca/problem/ccc24j5

note:
1. Use DFS / BFS algorithm, usually j5 each year is a graph traversal problem
2. try using a deque instead with BFS
'''

import sys

input = sys.stdin.readline  # fast input

N = int(input())
M = int(input())
grid = [input() for _ in range(N)]

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

start_r = int(input())
start_c = int(input())
stack = [(start_r, start_c)] 

visited = [[False] * M for _ in range(N)]   # for saving time, we dont need to revisit nodes

total = 0
gains = {"S": 1, "M": 5, "L": 10}   # use a dictionary, its helpful to know!

visited[start_r][start_c] = True
total += gains[grid[start_r][start_c]]

while stack:
    r, c = stack.pop()
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != "*" and not visited[nr][nc]: # at we out of bound? are we in a wall? have we been here before? 
            visited[nr][nc] = True
            total += gains[grid[nr][nc]]
            stack.append((nr, nc))

print(total)


