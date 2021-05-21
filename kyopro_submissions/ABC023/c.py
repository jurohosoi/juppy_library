# URL : https://atcoder.jp/contests/abc023/tasks/abc023_c

from collections import defaultdict

R, C, K = map(int, input().split())
N = int(input())

rc = []
r_cnt = defaultdict(int)
c_cnt = defaultdict(int)

for _ in range(N):
    r, c = map(int, input().split())
    r_cnt[r] += 1
    c_cnt[c] += 1
    rc.append((r, c))

c_cnt_inv = defaultdict(int)
for c in range(1, C+1):
    c_cnt_inv[c_cnt[c]] += 1

#print(c_cnt)
#print(c_cnt_inv)

ans = 0
for r in range(1, R+1):
    ans += c_cnt_inv[K - r_cnt[r]]

for r, c in rc:
    if r_cnt[r] + c_cnt[c] == K:
        ans -= 1
    if r_cnt[r] + c_cnt[c] == K+1:
        ans += 1

print(ans)