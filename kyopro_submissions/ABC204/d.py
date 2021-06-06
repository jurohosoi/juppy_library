N = int(input())
T = list(map(int,input().split()))
T.sort()

s = sum(T)
ok = 10**5
ng = 0

while ok - ng > 1:
    mid = (ok+ng)//2
    flag = False
    dp = [False]*(mid+1)
    dp[0] = True

    for e in T:
        for i in range(mid, -1, -1):
            if dp[i] and (i+e <= mid):
                dp[i+e] = True

    for i in range(mid, -1, -1):
        if dp[i]:
            if s-i <= mid:
                flag = True
            break
            
    if flag:
        ok = mid
    else:
        ng = mid
print(ok)