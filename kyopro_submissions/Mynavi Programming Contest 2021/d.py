# URL : https://atcoder.jp/contests/abc201/tasks/abc201_a

H, W = map(int,input().split())
A = [list(input()) for _ in range(H)]

dp = [[0]*W for _ in range(H)]

for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):
        if i == H-1 and j == W-1:
            continue
        ma = -10**9

        if i != H-1:
            tmp = dp[i+1][j]
            if A[i+1][j] == '+':
                tmp -= 1
            else:
                tmp += 1
            ma = max(ma, -tmp)
        
        if j != W-1:
            tmp = dp[i][j+1]
            if A[i][j+1] == '+':
                tmp -= 1
            else:
                tmp += 1
            ma = max(ma, -tmp)
        dp[i][j] = ma


if dp[0][0] == 0:
    print("Draw")
elif dp[0][0] > 0:
    print("Takahashi")
else:
    print("Aoki")