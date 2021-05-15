# URL : https://atcoder.jp/contests/abc201/tasks/abc201_b

N = int(input())
ST = []
for _ in range(N):
    s, t = map(str,input().split())
    ST.append((int(t), s))
ST.sort()

print(ST[-2][1])