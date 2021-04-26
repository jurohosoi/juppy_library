T, N, B, P = map(int, input().split())

for testcasenum in range(1, T+1):
    c = [0]*(N+1)
    c[0] = -1
    mi = 1
    for Q in range(N*B):
        D = int(input())
        ma = max(c)
        if ma < B-1:
            ret = c.index(ma)
            print(ret, flush=True)
            c[ret] += 1
        else:
            if D =

result = int(input())