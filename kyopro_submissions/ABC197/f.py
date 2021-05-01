# URL : https://atcoder.jp/contests/abc197/tasks/abc197_f
from collections import deque 

INF = 10**9
N, M = map(int, input().split())

def getpt(X, Y):
    if X <= Y:
        return X*N + Y
    return Y*N + X

# 辺の文字Cに対してord(C)-97したindexに(A, B)の頂点組が入っている
# 頂点組(A, B)を A*N + B で表す(A <= B )
chr_link = [[] for _ in range(26)]
edge_raw = []
for _ in range(M):
    A, B, C = map(str, input().split())
    A = int(A) - 1
    B = int(B) - 1
    if A > B:
        A, B = B, A
    chr_link[ord(C) - 97].append((A, B))
    edge_raw.append((A, B))

# from > to
edge = [[] for _ in range(N*N)]
for c in range(26):
    for i in range(len(chr_link[c])):
        a1, b1 = chr_link[c][i]
        for j in range(i+1, len(chr_link[c])):
            a2, b2 = chr_link[c][j]
            edge[getpt(a1, b2)].append(getpt(a2, b1))
            edge[getpt(a2, b1)].append(getpt(a1, b2))
            edge[getpt(a1, a2)].append(getpt(b1, b2))
            edge[getpt(b1, b2)].append(getpt(a1, a2))

# 01BFS
start = getpt(0, N-1)
dist = [INF]*(N**2)
dist[start] = 0
points = deque([start])
while points:
    now = points.popleft()
    for nxt in edge[now]:
        if dist[nxt] == INF:
            dist[nxt] = dist[now] + 1
            points.append(nxt)

ans = INF
for i in range(N):
    ans = min(ans, dist[getpt(i, i)]*2)
for a, b in edge_raw:
    ans = min(ans, dist[getpt(a, b)]*2 + 1)


if ans == INF:
    print(-1)
else:
    print(ans)