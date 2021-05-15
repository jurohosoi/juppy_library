# URL : https://atcoder.jp/contests/abc201/tasks/abc201_e

import sys
input = sys.stdin.buffer.readline

MOD = 10**9 + 7
N = int(input())

edge = [[] for _ in range(N)]
for i in range(1, N):
    u, v, w = map(int,input().split())
    edge[u-1].append((v-1, w))
    edge[v-1].append((u-1, w))
    
Wi = [-1]*N
chi = [[] for _ in range(N)]
order = []
tank = [0]

while tank:
    now = tank.pop()
    
    flag = False
    for nxt, w in edge[now]:
        if nxt == 0:
            continue
        if Wi[nxt] == -1:
            chi[now].append(nxt)
            Wi[nxt] = w
            tank.append(nxt)
            flag = True
    if flag:
        order.append(now)
order = order[::-1]

ans = 0
one = [0]*N
zero = [0]*N
for bitflag in range(60):
    tmp = 0
    for e in order:
        A_s = 0
        B_s = 0
        for c in chi[e]:
            if (Wi[c] >> bitflag)&1 == 0:
                A_s += one[c]
                B_s += zero[c] + 1
            else:
                A_s += zero[c] + 1
                B_s += one[c]
            A_s %= MOD
            B_s %= MOD
        tmp += A_s
        for c in chi[e]:
            if (Wi[c] >> bitflag)&1 == 0:
                tmp = (tmp + one[c] * (B_s-zero[c]-1)) %MOD
            else:
                tmp = (tmp + (zero[c] + 1) * (B_s - one[c])) %MOD
        one[e] = A_s
        zero[e] = B_s
    ans = (ans + (tmp<<bitflag))%MOD
print(ans % MOD)

