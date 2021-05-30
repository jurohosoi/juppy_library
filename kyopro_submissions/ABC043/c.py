# URL : https://atcoder.jp/contests/abc043/tasks/arc059_a

N = int(input())
a = list(map(int, input().split()))

ans = 10**7
for x in range(-100, 101):
    cost = 0
    for elt in a:
        cost += (elt - x)**2
    ans = min(ans, cost)
print(ans)