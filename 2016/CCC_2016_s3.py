from collections import deque, defaultdict
import sys

input = sys.stdin.read
sys.setrecursionlimit(10**6)

# ===== Problem overview / approach ============================================
# 1) PRUNE: Keep only the minimal subtree that connects all pho nodes
#    We can do this by a DFS that marks every node
#    that lies on a path to some pho node. After pruning, "pho[v] == True" means
#    node v is kept in the pruned tree (either it is a pho restaurant or it is
#    on a connecting path between pho restaurants).
# 2) DIAMETER: The minimal walk to visit all kept nodes equals:
#       2 * (#_of_edges_in_the_pruned_tree) - diameter_of_pruned_tree
#    because a full “double-counted” traversal of the pruned tree costs
#    2 * edges, but we can save distance equal to the tree diameter by
#    not having to backtrack along the longest path.
#
# Implementation details below:
#   - We store the graph 1-indexed (original input is 0-indexed; we add +1).
#   - After the pruning DFS, sum(pho) gives the number of nodes in the *pruned*
#     tree (note this includes originally-non-pho nodes that lie on paths).
#   - For BFS we only traverse nodes with pho == True (i.e., within the pruned tree).
#   - Two BFS passes find the diameter of the pruned tree.
# ==============================================================================

# constants
MM = int(1e5) + 1   # Maximum array size for this problem constraints.

# globals (kept as in original code for speed/simple sharing across functions)
n, m = 0, 0
re, longest, node_needed = 0, 0, 0
dist = [0] * MM         # Distance array reused by BFS passes.
pho = [False] * MM      # Before DFS: original pho nodes are True.
                        # After DFS: True means "node is kept in pruned tree".
visited = [False] * MM  # For quicker run time
adj = defaultdict(list) # Adjacency list for the tree.
pre = {}                # Parent pointers from BFS2 

# ----------------------------- PRUNING DFS ------------------------------------
def dfs(node, prev):
    """
    DFS that propagates 'pho' markings up the tree:
    - If a child subtree contains a kept node (pho[...] == True),
      mark the current node as kept as well.
    - We start DFS from any pho node; the propagation ensures 'pho[v]'
      is True exactly for nodes in the minimal subtree connecting all pho nodes.
    """
    for nxt in adj[node]:
        if nxt == prev:
            continue
        dfs(nxt, node)
        # If the child is kept (either a pho restaurant or on a path to one),
        # then this node must also be kept to connect them.
        if pho[nxt]:
            pho[node] = True



# ----------------------------- BFS on PRUNED TREE -----------------------------
def bfs(node):
    """
    BFS restricted to the pruned tree (we only traverse nodes with
    pho[...] == True). Fills 'dist' from 'node' and updates the global 'longest'
    as the maximum distance reached.
    """
    global longest
    visited[:] = [False] * MM
    dist[:] = [0] * MM

    visited[node] = True
    dist[node] = 0
    deq = deque([node])

    while deq:
        cur = deq.popleft()
        for nxt in adj[cur]:
            # Only traverse inside the pruned tree
            if not visited[nxt] and pho[nxt]:
                visited[nxt] = True
                deq.append(nxt)
                dist[nxt] = dist[cur] + 1

    # 'dist' is zero for unvisited nodes; taking max(dist) is fine because
    # all relevant (kept) nodes reachable from 'node' have correct distances.
    longest = max(dist)

# ----------------------------- DIAMETER BFS -----------------------------------
def bfs2(node):
    """
    Another BFS on the pruned tree that also tracks parents.
    We use it to find the farthest node and the exact diameter length:
      - Start from one endpoint found by the first BFS,
      - The farthest node from it is the other endpoint of the diameter.
    The length of that path is stored in 'longest', and its endpoint index in
    'node_needed'. 
    """
    global longest, node_needed
    visited[:] = [False] * MM
    dist[:] = [0] * MM

    visited[node] = True
    dist[node] = 0
    deq = deque([node])

    while deq:
        cur = deq.popleft()
        for nxt in adj[cur]:
            if not visited[nxt] and pho[nxt]:
                visited[nxt] = True
                deq.append(nxt)
                dist[nxt] = dist[cur] + 1
                pre[nxt] = cur  

    longest = max(dist)              # Diameter length from this BFS.
    node_needed = dist.index(longest)  # One endpoint of the diameter.

def main():
    global n, m, re

    # Read all input at once for speed in CP; then parse manually.
    data = input().split()
    n, m = int(data[0]), int(data[1])
    # ----------------------- Read pho restaurants ------------------------------
    # Input pho IDs are 0-indexed in CCC; we store them 1-indexed.
    pho_indices = list(map(int, data[2:m+2]))
    for re in pho_indices:
        pho[re + 1] = True
    # ----------------------------- Read edges ----------------------------------
    # There are (n - 1) edges following the pho list.
    edges = data[m+2:]
    for i in range(0, len(edges), 2):
        x, y = int(edges[i]), int(edges[i+1])
        adj[x + 1].append(y + 1)
        adj[y + 1].append(x + 1)

    # -------------------------- Step 1: Prune ----------------------------------
    # Run DFS from any pho node, I picked the first pho node
    # After this, 'pho[v] == True' iff v is in the pruned subtree.
    dfs(pho_indices[0] + 1, -1)

    # Count of nodes kept after pruning
    num_pho = sum(pho)

    # -------------------------- Step 2: BFS endpoint ---------------------------
    # Find a farthest kept node from an arbitrary kept node
    bfs(pho_indices[0] + 1)
    next_node = dist.index(longest)

    # -------------------------- Step 3: Diameter -------------------------------
    # Run BFS again from that farthest endpoint to get the diameter of the
    # pruned tree (length of the longest kept-kept path).
    bfs2(next_node)

    # -------------------------- Final answer -----------------------------------
    print((2 * (num_pho - 1)) - longest)

main()
