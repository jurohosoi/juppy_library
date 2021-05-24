# URL : https://atcoder.jp/contests/arc120/tasks/arc120_a

N = int(input())
A = list(map(int,input().split()))
s = 0
plus = 0
ma = -1

for i in range(N):
    s += A[i]
    ma = max(ma, A[i])

    ans = s + ma*(i+1) + plus
    plus += s
    
    print(ans)