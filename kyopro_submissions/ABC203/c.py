# URL : https://atcoder.jp/contests/abc203/tasks/abc203_c

N, K = map(int, input().split())
AB = []
for _ in range(N):
    A, B = map(int, input().split())
    AB.append((A, B))
AB.sort()

now = 0
money = K
idx = 0

while True:
    if idx == N:
        now += money
        money = 0
        break
    if now >= AB[idx][0]:
        money += AB[idx][1]
        idx += 1
    elif money != 0:
        now += money
        money = 0
    else:
        break

print(now)
