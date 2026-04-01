import sys
import heapq

# This solution finds the minimum total cost to travel from room 1 to room n.
# Each tunnel has a weight, and changing tunnels costs the absolute difference
# between the previous tunnel’s weight and the new tunnel’s weight.
#
# We treat each state as (cost_so_far, current_room, last_edge_used).
# The cost of the next step depends on the weight of the last tunnel used,
# so we must track it.
#
# We build an adjacency list graph[u] = [(neighbor, edge_index)] and an array
# edges[i] = weight of edge i. We also add a "virtual edge" with weight 0 for
# the start so the first step costs |0 - w_first|.
#
# We use Dijkstra’s algorithm with a min-heap priority queue:
#   - Each heap entry is (cost, room, last_edge_index).
#   - We always process the state with the lowest total cost so far.
#   - For each tunnel j leaving the current room:
#       new_cost = cost + abs(weight_of_last_edge - weight_of_j)
#     If this new_cost is better than what we’ve seen for j, we push it.
#
# As soon as we pop a state where room == n, that cost is the minimum possible.



data = sys.stdin.read().strip().split()
it = iter(data)
n = int(next(it))     # number of rooms (nodes)
m = int(next(it))     # number of tunnels (edges)

''' 
graph[u] = list of (v, edge_index that connects u-v)
edges[u] = weight of edge_index u

4 3
1 2 3   Edge 0: connects 1-2, weight 3
2 3 5   Edge 1: connects 2-3, weight 5
3 4 2   Edge 2: connects 3-4, weight 2

so: 
edges[0] = 3
edges[1] = 5
edges[2] = 2
graph[1] = [(2, 0)]
graph[2] = [(1, 0), (3, 1)]
graph[3] = [(4, 2), (2, 1)]
graph[4] = [(3, 2)]
'''
graph = [[] for _ in range(n + 1)]

# edges[e] = weight of edge e; we also use a "virtual" edge at index m
# for the starting state, whose weight is 0 by default.
edges = [0] * (m + 1)

# Read edges; assign indices 0..m-1
for i in range(m):
    u = int(next(it)); v = int(next(it)); w = int(next(it))
    graph[u].append((v, i))
    graph[v].append((u, i))
    edges[i] = w

# Min-heap priority queue for Dijkstra
pq = []

# best[e] = best known total cost to reach any node with last_edge_index = e
# (We track per-edge because the next step's cost depends only on the last edge weight.)
INF = float('inf')
best = [INF] * (m + 1)

# vis[e] == True means we've popped (finalized) the minimal cost among
# all states whose last_edge_index is e (Dijkstra "visited" by edge index).
vis = [False] * (m + 1)

# Start at node 1 with "virtual" previous edge m of weight 0.
# This makes the first real step pay |0 - w_first|.
heapq.heappush(pq, (0, 1, m))  # (cost_so_far, current_room, last_edge_index)

while pq:
    c, a, i = heapq.heappop(pq)

    # If we've already finalized states ending with last-edge i, skip.
    if vis[i]:
        continue
    vis[i] = True

    # If we reached node n, by Dijkstra this cost is minimal; print and exit.
    if a == n:
        print(c)
        sys.exit()

    # Try all outgoing real edges j from current node a.
    for neighbour in graph[a]:
        b, j = neighbour
        if vis[j]:
            continue  # last-edge j already finalized
        # Cost to retune boots from weight edges[i] to edges[j]
        new_c = c + abs(edges[i] - edges[j])
        # If this is the best total cost we've seen for last-edge j, push it.
        if new_c < best[j]:
            best[j] = new_c
            heapq.heappush(pq, (new_c, b, j))