# URL : https://atcoder.jp/contests/abc198/tasks/abc198_e

MAX_C = 10**5+5
N = int(input())
C = list(map(int, input().split()))

edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    # 0-indexed
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

# parent vertex, children list
par = [-1]*N
chi = [[] for _ in range(N)]
vertextank = [0]
while vertextank:
    now = vertextank.pop()
    for nextv in edges[now]:
        if nextv != 0 and par[nextv] == -1:
            par[nextv] = now
            chi[now].append(nextv)
            vertextank.append(nextv)

# Euler Tour
ans = []
colorcounter = [0]*MAX_C
eulertank = [0]
while eulertank:
    q = eulertank.pop()
    if q >= 0:
        #first time
        if colorcounter[C[q]] == 0:
            ans.append(q+1) # 1-indexed
        colorcounter[C[q]] += 1
        eulertank.append(~q)
        for ch in chi[q]:
            eulertank.append(ch)
    else:
        colorcounter[C[~q]] -= 1

ans.sort()
print(*ans, sep='\n')