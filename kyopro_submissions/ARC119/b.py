# URL : https://atcoder.jp/contests/arc119/tasks/arc119_b

N = int(input())
S = list(input())
T = list(input())

s_zero = []
t_zero = []
for i in range(N):
    if S[i] == '0':
        s_zero.append(i)
    if T[i] == '0':
        t_zero.append(i)

if len(s_zero) != len(t_zero):
    print(-1)
else:
    ans = 0
    for i in range(len(s_zero)):
        if s_zero[i] != t_zero[i]:
            ans += 1
    print(ans)