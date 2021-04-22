# URL : https://atcoder.jp/contests/jsc2021/tasks/jsc2021_b

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans = []
for Aelt in A:
    if not Aelt in B:
        ans.append(Aelt)
for Belt in B:
    if not Belt in A:
        ans.append(Belt)

print(*sorted(ans))