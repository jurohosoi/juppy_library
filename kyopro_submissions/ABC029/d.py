# URL : https://atcoder.jp/contests/abc029/tasks/abc029_d

N = int(input())
ans = 0

# dg桁に1が何回出てくるか
for dg in range(10):
    block, frag = divmod(N, 10**(dg+1))
    ans += block * (10**dg) + min(10**dg, max(0, frag-10**dg+1))
print(ans)