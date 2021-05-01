from collections import deque
S = list(input())

ans = deque([])
flag = 1
for e in S:
    if e == "R":
        flag *= -1
    elif flag > 0:
        ans.append(e)
    else:
        ans.appendleft(e)
if flag > 0:
    ans = list(ans)
else:
    ans = list(ans)[::-1]

res = []
for e in ans:
    res.append(e)
    while len(res) >= 2:
        if res[-1] != res[-2]:
            break
        res.pop()
        res.pop()

print("".join(res))