"""
https://dmoj.ca/problem/ccc20s2
"""

# !Note! this solution TLE on the last test batch.
# I think its because I used DFS
# The issue can likely be solved by using a large pre-filled
# visited array instead of the current visited set.
# Refer to j5.cpp for final solution.

rows = int(input())
cols = int(input())
graph = []

for i in range(rows):
    graph.append(list(map(int, input().split(" "))))
dest = graph[rows-1][cols-1]
starting = graph[0][0]

def findNeighbors(chart, width, height, val, explored):
    mults = []
    for i in range(val):
        n = i+1
        if val % n == 0:
            if n <= width and val/n <= height:
                tempList = [n, int(val/n)]
                if tempList not in explored:
                    mults.append(tempList)
    return mults

def findMults(chart, width, height, start):
    if len(graph) > 10000:
        return "no"
    explored = []
    stack = [[[1,1], start]]
    while stack:
        node, val = stack.pop(0)
        if node[0] == width and node[1] == height:
            return "yes"
        explored.append(node)
        neighbors = findNeighbors(chart, width, height, val, explored)
        for neighbor in neighbors:
            if neighbor not in explored:
                stack.append([neighbor, chart[neighbor[1]-1][neighbor[0]-1]])
    return "no"

print(findMults(graph, cols, rows, starting))