import io, os, heapq
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

R, C = map(int,input().split())
N = R*C

edge = [[] for i in range(N)]
for i in range(R):
    a = list(map(int,input().split()))
    for j in range(C-1):
        edge[i*C + j].append((a[j]<<20) + i*C + j+1)
        edge[i*C + j+1].append((a[j]) + i*C + j)

for i in range(R-1):
    b = list(map(int,input().split()))
    for j in range(C):
        edge[i*C + j].append(b[j] * N + (i+1)*C + j)

for i in range(R):
    for j in range(C):
        for k in range(1, i+1):
            edge[i*C + j].append((1+k) * N + (i-k)*C + j)

dist = [-1]*N
goal = (R-1)*C + (C-1)
tank = [0]
while tank:
    val = heapq.heappop(tank)
    d, now = divmod(val, N)
    if dist[now] != -1:
        continue
    dist[now] = d
    if now == goal:
        break
    for nxtval in edge[now]:
        cost, nxt = divmod(nxtval, N)
        if dist[nxt] == -1:
            heapq.heappush(tank, (d+cost)*N + nxt)

print(dist[goal])