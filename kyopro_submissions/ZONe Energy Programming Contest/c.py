N = int(input())
V = []
for _ in range(N):
    V.append(tuple(map(int,input().split())))

ok = 0
ng = 10**9+1

while (ng-ok) > 1:
    mid = (ok+ng)//2

    S = [[False]*32 for i in range(4)]
    S[0][0] = True

    for i in range(1, 4):
        for ve in V:
            bitflag = 0
            for j in range(5):
                if ve[j] >= mid:
                    bitflag = bitflag | (1<<j)
            for j in range(32):
                if S[i-1][j]:
                    S[i][j | bitflag] = True
    if S[-1][-1]:
        ok = mid
    else:
        ng = mid

print(ok)