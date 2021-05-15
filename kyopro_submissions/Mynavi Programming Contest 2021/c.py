# URL : https://atcoder.jp/contests/abc201/tasks/abc201_c

S = list(input())
ans = 0

for i in range(10000):
    flag = True
    tank = []
    for j in range(4):
        num = (i//(10**j)) % 10
        if S[num] == 'x':
            flag = False
        tank.append(num)
    for j in range(10):
        if S[j] == 'o' and (not j in tank):
            flag = False
    #print(i, tank)
    if flag:
        ans += 1

print(ans)