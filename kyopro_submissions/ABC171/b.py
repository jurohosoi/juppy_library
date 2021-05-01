# # URL : https://atcoder.jp/contests/abc171/tasks/abc171_b

N, K = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
print(sum(p[:K]))