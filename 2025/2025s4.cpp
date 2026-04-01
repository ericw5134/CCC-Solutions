#include <bits/stdc++.h>
using namespace std;

using ll = long long;
// Each state in the priority queue: (total_cost_so_far, current_node, last_edge_index)
using State = tuple<ll, ll, ll>;


int vis[200001];          // vis[e] == 1 means we've finalized the best cost for states whose last edge is e
int edges[200001];        // edges[e] = weight of edge e

// Adjacency list: for each node, store (neighbor, edge_index)
// Edge indices are 0..m-1
vector<pair<ll, ll>> graph[200001];

int main() {
    int n, m; 
    cin >> n >> m;

    // Read edges. We give every edge an index i (0..m-1).
    // For each endpoint, push (other_endpoint, edge_index) into the graph.
    for (int i = 0; i < m; i++) {
        int u, v, w; 
        cin >> u >> v >> w;
        graph[u].push_back({v, i});
        graph[v].push_back({u, i});
        edges[i] = w;  // store the edge weight
    }
    
    // Min-heap for Dijkstra (priority queue of smallest cost first)
    priority_queue<State, vector<State>, greater<>> pq;

    // best[e] = best known cost to reach *some node* with last edge index = e
    // (We only need m entries, but we also use a virtual start edge m, so size m+1.)
    vector<ll> best(m + 1, LLONG_MAX);
    
    // Start at node 1 with a "virtual" previous edge = m whose weight is implicitly 0
    // (edges[m] is 0 because global arrays are zero-initialized; we never set edges[m] otherwise.)
    pq.push({0, 1, m});
    
    while (!pq.empty()) {
        auto [c, a, i] = pq.top(); 
        pq.pop();
        
        // Standard Dijkstra "visited" check, but keyed by last_edge_index.
        // Once we pop an edge index i for the first time, we’ve finalized the
        // minimal cost among all states whose last edge is i.
        if (vis[i]) continue;
        vis[i] = 1;
        
        // If we've reached node n, the popped cost c is minimal—return it.
        if (a == n) {
            cout << c;
            return 0;
        }
        
        // Try all outgoing edges j from current node a
        for (auto [b, j] : graph[a]) {
            if (vis[j]) continue;  // if last-edge state j already finalized, skip

            // Cost to switch boots from previous edge weight edges[i] to this edge weight edges[j]
            ll new_c = c + llabs((ll)edges[i] - (ll)edges[j]);

            // If this is the best way seen so far to end with last edge j, push it
            if (new_c < best[j]) {
                best[j] = new_c;
                // New state: at node b, having just used edge j, with total cost new_c
                pq.push({new_c, b, j});
            }
        }
    }
}
