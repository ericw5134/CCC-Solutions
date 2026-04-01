'''
https://dmoj.ca/problem/ccc18s3

note:
1. use BFS 
2. it is possible for you to spawn in a camera's view
3. it is possible for conveyor belts to loop you around in a circle (need a way to break a cycle in a graph)
WWWWWWW
WRRRRDW
WUWSWDW
WULLLLW
WWWWWWW    as an example
'''

from collections import deque

MAX = 108
INF = float('inf')

n, m = 0, 0
start = (0, 0)
grid = [[''] * MAX for _ in range(MAX)]
dist = [[INF] * MAX for _ in range(MAX)]
vis = [[False] * MAX for _ in range(MAX)]
cameras = []
queries = []

def camera_spread():
    global cameras, grid, dist, vis, n, m
    for camera in cameras:
        # Camera scanning upwards
        for i in range(camera[0], 0, -1):
            if grid[i][camera[1]] == 'W': break
            if grid[i][camera[1]] == '.':
                dist[i][camera[1]] = -10
                vis[i][camera[1]] = True
        # Camera scanning downwards
        for i in range(camera[0], n + 1):
            if grid[i][camera[1]] == 'W': break
            if grid[i][camera[1]] == '.' or grid[i][camera[1]] == 'S':
                dist[i][camera[1]] = -10
                vis[i][camera[1]] = True
        # Camera scanning leftwards
        for i in range(camera[1], 0, -1):
            if grid[camera[0]][i] == 'W': break
            if grid[camera[0]][i] == '.' or grid[camera[0]][i] == 'S':
                dist[camera[0]][i] = -10
                vis[camera[0]][i] = True
        # Camera scanning rightwards
        for i in range(camera[1], m + 1):
            if grid[camera[0]][i] == 'W': break
            if grid[camera[0]][i] == '.' or grid[camera[0]][i] == 'S':
                dist[camera[0]][i] = -10
                vis[camera[0]][i] = True

def bfs(start):
    global grid, dist, vis, n, m
    deq = deque([start])
    while deq:
        cur = deq.popleft()
        x, y = cur
        if vis[x][y]: continue
        if grid[x][y] == 'W' or grid[x][y] == 'C': continue

        if grid[x][y] in {'S', '.'}:
            if y > 1 and dist[x][y - 1] > dist[x][y] + 1:
                dist[x][y - 1] = dist[x][y] + 1
                deq.append((x, y - 1))
            if y < m and dist[x][y + 1] > dist[x][y] + 1:
                dist[x][y + 1] = dist[x][y] + 1
                deq.append((x, y + 1))
            if x > 1 and dist[x - 1][y] > dist[x][y] + 1:
                dist[x - 1][y] = dist[x][y] + 1
                deq.append((x - 1, y))
            if x < n and dist[x + 1][y] > dist[x][y] + 1:
                dist[x + 1][y] = dist[x][y] + 1
                deq.append((x + 1, y))
        elif grid[x][y] == 'L' and y > 1 and grid[x][y - 1] != 'W' and dist[x][y - 1] > dist[x][y]:
            dist[x][y - 1] = dist[x][y]
            deq.append((x, y - 1))
        elif grid[x][y] == 'R' and y < m and grid[x][y + 1] != 'W' and dist[x][y + 1] > dist[x][y]:
            dist[x][y + 1] = dist[x][y]
            deq.append((x, y + 1))
        elif grid[x][y] == 'U' and x > 1 and grid[x - 1][y] != 'W' and dist[x - 1][y] > dist[x][y]:
            dist[x - 1][y] = dist[x][y]
            deq.append((x - 1, y))
        elif grid[x][y] == 'D' and x < n and grid[x + 1][y] != 'W' and dist[x + 1][y] > dist[x][y]:
            dist[x + 1][y] = dist[x][y]
            deq.append((x + 1, y))

def main():
    global n, m, start, grid, dist, vis, queries, cameras
    n, m = map(int, input().split())
    
    for i in range(1, n + 1):
        row = input().strip()
        for j in range(1, m + 1):
            grid[i][j] = row[j - 1]
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == '.':
                queries.append((i, j))
            elif grid[i][j] == 'C':
                cameras.append((i, j))

    # Set distances to infinity initially
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dist[i][j] = INF

    camera_spread()
    dist[start[0]][start[1]] = 0
    bfs(start)

    for q in queries:
        if vis[q[0]][q[1]] or dist[q[0]][q[1]] >= INF:
            print(-1)
        else:
            print(dist[q[0]][q[1]])


main()


