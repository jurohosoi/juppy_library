# URL : https://atcoder.jp/contests/arc118/tasks/arc118_a

t, N = map(int, input().split())

# t*A >= N*100を満たす最小のint_A

ok = 10**12
ng = 0
while ok - ng > 1:
    mid = (ok+ng)//2
    if t*mid >= N*100:
        ok = mid
    else:
        ng = mid

print(ok + t*ok//100 - 1)