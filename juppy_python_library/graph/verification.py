"""
verify : https://atcoder.jp/contests/abc035/submissions/20241454
"""
import heapq

class Graph:
    
    def __init__(self, maxsize=10**6, edgetype='cost_tuple'):
        """
        nodes : 0, 1, 2, ... , n-1

        edges[node_from] describes edges from node_from

        Edge type(edgetype) defines the type of element of edges  : 
            'cost_mod'   -- cost*n + node_to
            'cost_tuple' -- (cost, node_to)
            'unweighted' -- node_to
        """
        self._n = maxsize # number of nodes
        self._edges = [[] for _ in range(self._n)] # adjacency list
        self._edgetype = edgetype # edgetype

    def edgeadd(self, a, b, cost=None, directed=False):
        """Add edge
        directed   : a ---> b (cost)
        undirected : a <--> b (cost)
        """
        if self._edgetype == 'cost_tuple':
            self._edges[a].append((cost, b))
            if not directed:
                self._edges[b].append((cost, a))
        elif self._edgetype == 'cost_mod':
            self._edges[a].append(cost*self._n + b)
            if not directed:
                self._edges[b].append(cost*self._n + a)
        elif self._edgetype == 'unweighted':
            self._edges[a].append(b)
            if not directed:
                self._edges[b].append(a)
    
    def dijkstra(self, node_start, initval=float("inf")):
        """
        Return shoretet distance from node_start
        """
        dist_dijkstra = [initval]*self._n
        
        heapnode_dist = [node_start]
        while heapnode_dist:
            nodedist_now = heapq.heappop(heapnode_dist)
            dist_now, node_now = divmod(nodedist_now, self._n)
            
            if dist_dijkstra[node_now] != initval:
                continue
            dist_dijkstra[node_now] = dist_now
            
            for edge_nxt in self._edges[node_now]:
                cost_nxt, node_nxt = divmod(edge_nxt, self._n)
                if dist_dijkstra[node_nxt] != initval:
                    continue
                heapq.heappush(heapnode_dist, (dist_now+cost_nxt)*self._n + node_nxt)
        return dist_dijkstra
    
def solve():
    # input
    N, M, T = map(int,input().split())
    A = list(map(int,input().split()))

    # Construct
    G = Graph(maxsize = N, edgetype='cost_mod')
    G_inv = Graph(maxsize = N, edgetype='cost_mod')
    for _ in range(M):
        a, b, c = map(int,input().split())
        G.edgeadd(a-1, b-1, c, directed=True)
        G_inv.edgeadd(b-1, a-1, c, directed=True)
    d_fr_start = G.dijkstra(0, initval=1<<30)
    d_to_goal = G_inv.dijkstra(0, initval=1<<30)

    # Calculate max money
    maxmoney = 0
    for node_stay in range(N):
        money_tmp = max(0, T - d_fr_start[node_stay] - d_to_goal[node_stay])
        maxmoney = max(maxmoney, money_tmp*A[node_stay])
    
    # Output
    print(maxmoney)

if __name__ == '__main__':
    solve()
    