#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <algorithm>

using namespace std;

const int INF = numeric_limits<int>::max();

typedef pair<int, int> pie;

vector<int> dijkstra(const vector<vector<pie>>& G, int s, int f, vector<int>& parents) {
    int n = G.size();
    vector<int> dists(n, INF);
    priority_queue<pie, vector<pie>, greater<pie>> pq;
    
    dists[s] = 0;
    pq.push({0, s});
    
    while (!pq.empty()) {
        int curr = pq.top().second;
        int dist = pq.top().first;
        pq.pop();
        
        if (dist > dists[curr]) continue;
        
        for (const auto& [next, weight] : G[curr]) {
            if (dists[next] > dists[curr] + weight) {
                dists[next] = dists[curr] + weight;
                parents[next] = curr;
                pq.push({dists[next], next});
            }
        }
    }
    return dists;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> cities(n);
    for (int i = 0; i < n; i++) {
        cin >> cities[i];
    }
    
    vector<vector<pie>> graph(n);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--; // Convert to 0-indexed
        int weight = (cities[a] != cities[b]) ? 1 : 0;
        graph[a].emplace_back(b, weight);
        graph[b].emplace_back(a, weight);
    }
    
    int start = 0, end = n - 1;
    vector<int> parents(n);
    for (int i = 0; i < n; i++) parents[i] = i;
    
    vector<int> dists = dijkstra(graph, start, end, parents);
    
    if (dists[end] != INF) {
        vector<int> path;
        int curr = end;
        while (true) {
            path.push_back(curr + 1);
            if (curr == start) break;
            curr = parents[curr];
        }
        reverse(path.begin(), path.end());
        
        cout << dists[end] << " " << path.size() << endl;
        for (size_t i = 0; i < path.size(); i++) {
            cout << path[i];
            if (i < path.size() - 1) cout << " ";
        }
        cout << endl;
    } else {
        cout << "impossible" << endl;
    }
    
    return 0;
}
