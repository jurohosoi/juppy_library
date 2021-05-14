# URL : https://atcoder.jp/contests/abc175/tasks/abc175_c

X, K, D = map(int, input().split())

ans = []
ans.append(abs(X - K*D))
ans.append(abs(X + K*D))

X = abs(X)

if K*D >= X:
    k_ = X//D
    rest = K - k_
    x = X - k_ * D

    if rest % 2 == 0:
        ans.append(x)
    else:
        ans.append(abs(x - D))

print(min(ans))