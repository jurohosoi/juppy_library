import sys, heapq
input = sys.stdin.buffer.readline
N, M = map(int, input().split())

def calc_cost(p, c, d):
    # min( c+w+[d//(w+p+1)])
    high = max(d - p, 1)
    low = 0
    for _ in range(40):
        mid_left = high/3+low*2/3
        mid_right = high*2/3+low/3
        if mid_left + d/(mid_left+p+1) >= mid_right + d/(mid_right+p+1):
            low = mid_left
        else:
            high = mid_right
    ret = 10**20

    for i in range(max(0, int(low-10)), int(high+10)):
        if ret > c + i + d//(i+p+1):
            ret = c + i + d//(i+p+1)
    return ret

edge = [[] for _ in range(N)]
for _ in range(M):
    A, B, C, D = map(int, input().split())
    edge[A-1].append((B-1, C, D))
    edge[B-1].append((A-1, C, D))

dist = [-1]*N
tank = [0]
nonvisit = [True]*N
dist[0] = 0


while tank:
    val = heapq.heappop(tank)
    cost, now = divmod(val, N)
    print(now)
    if nonvisit[now]:
        nonvisit[now] = False
    else:
        continue

    for nxt_v, c, d in edge[now]:
        if not nonvisit[nxt_v]:
            continue
        nxt_cost = cost + calc_cost(cost, c, d)
        #print(now, nxt_v, nxt_cost)
        if dist[nxt_v] == -1 or nxt_cost < dist[nxt_v]:
            dist[nxt_v] = nxt_cost
            heapq.heappush(tank, nxt_cost*N + nxt_v)
print(dist[-1])
