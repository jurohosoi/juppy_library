N, D, H = list(map(int,input().split()))
ans = 0.0

for _ in range(N):
    d, h = map(int,input().split())
    x = (D*h-d*H)/(H-h)
    ans = max(ans, x*H/(x+D))

print(ans)