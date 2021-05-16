# URL : https://atcoder.jp/contests/abc171/tasks/abc171_c

N = int(input())
N -= 1

ans = []

for i in range(30):
    if i == 0:
        val = N%26
        ans.append(chr(97 + val))
    else:
        if N == 0:
            break
        N -= 1
        val = N%26
        ans.append(chr(97 + val))
    N //= 26
ans.reverse()
print(''.join(ans))

    