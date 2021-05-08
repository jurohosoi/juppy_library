# URL : https://atcoder.jp/contests/abc200/tasks/abc200_c

N = int(input())
A = list(map(int,input().split()))

cnt = dict()
ans = 0

for e in A:
    if e%200 in cnt:
        ans += cnt[e%200]
    
    if e%200 in cnt:
        cnt[e%200] += 1
    else:
        cnt[e%200] = 1 

print(ans)