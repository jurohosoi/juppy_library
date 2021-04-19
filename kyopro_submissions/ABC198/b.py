# URL : https://atcoder.jp/contests/abc198/tasks/abc198_b

N = list(input())

zero_right_index = len(N) # 右端から連続している0の最小index
for i in range(len(N)-1, -1, -1):
    if N[i] == '0':
        zero_right_index = i
    else:
        break

flag = True # 回文かのflag
for i in range(zero_right_index):
    if N[i] != N[zero_right_index - i - 1]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")