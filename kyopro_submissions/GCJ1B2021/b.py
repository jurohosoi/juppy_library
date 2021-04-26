
MAX_RES = 2000
T = int(input())

for testcasenum in range(1, T+1):
    N, A, B = map(int, input().split())
    U = list(map(int, input().split())) + [0]*B
    res = -1
    for i in range(N-1, B-1, -1):
        if U[i] > 0:
            U[i - A] += U[i]
            U[i - B] += U[i]
            U[i] = 0
    #print(U)
    if sum(U) == 1:
        res = U.index(1) + 1
    else:
        now = [[0]*B for _ in range(MAX_RES)]
        for i in range(B):
            now[i][i] = 1
        for trial in range(B, MAX_RES):
            flag = True
            plus = [0]*B
            for i in range(B):
                now[trial][i] = now[trial-A][i] + now[trial-B][i]
            for i in range(B-1, -1, -1):
                if U[i] > now[trial][i] + plus[i]:
                    flag = False
                else:
                    if i-A >= 0:
                        plus[i-A] += now[trial][i] - U[i]
                    if i-B >= 0:
                        plus[i-B] += now[trial][i] - U[i]
            if flag:
                res = trial + 1
                break
            #print(now[trial])        
    if res != -1:
        print("Case #{}: {}".format(testcasenum, res))
    else:
        print("Case #{}: IMPOSSIBLE".format(testcasenum))
