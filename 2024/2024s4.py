'''
https://dmoj.ca/problem/ccc24s4
'''

import sys

sys.setrecursionlimit(300000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

colors = ["G"] * M  # initialize all edges as "G" (uncolored)
visited = [False] * (N + 1) # track visited nodes

def solve(cur, parity): # parity is like a toggle switch (0 -> "B", 1 -> 'R')
    for adj, edge in graph[cur]:
        if visited[adj]:
            continue
        visited[adj] = True
        colors[edge] = "R" if parity else "B"   # alternate betweeb "R" and "B", make sure no adjacent edges have the same colour
        solve(adj, parity ^ 1)  # DFS continues until all reachable nodes are visited


for i in range(1, N + 1):
    if visited[i]:
        continue
    visited[i] = True
    solve(i, 0) # if a node is unvisited, start a new DFS traversal
                # in case we have multiple disconnected graphs

print("".join(colors))