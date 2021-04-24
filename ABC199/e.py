# URL : https://atcoder.jp/contests/abc199/tasks/abc199_e

N, M = map(int, input().split())
XYZ = [[] for _ in range(N)]
for _ in range(M):
    X, Y, Z = map(int,input().split())
    XYZ[X].append((Y, Z))

dp = [[0]*(2**N) for _ in range(N+1)]
cnt = [0]*(N+1)
oldbit = set([0])
dp[0][0] = 1
for k in range(N):
    newbit = oldbit
    oldbit = set()
    for flag in newbit:
        nxtset = set()
        for i in range(N):
            if (flag >> i) & 1 == 1:
                cnt[i+1] += 1
            else:
                nxtset.add(i)
        for i in range(1, N):
            cnt[i] += cnt[i-1]
        for nxt in nxtset:
            judge = True
            for Y, Z in XYZ[k]:
                if cnt[Y] > Z:
                    judge = False
                    break
            if judge:
                oldbit.add(flag + (1<<nxt))
                dp[k+1][flag + (1<<nxt)] += dp[k][flag]
        for i in range(1, N+1):
            cnt[i] = 0
print(dp[-1][-1])