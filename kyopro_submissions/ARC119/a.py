# URL : https://atcoder.jp/contests/arc119/tasks/arc119_a

N = int(input())

ans = 10**16
b2 = 1

for b in range(100):
    a, c = divmod(N, b2)
    b2 *= 2
    ans = min(ans, a + b + c)

print(ans)