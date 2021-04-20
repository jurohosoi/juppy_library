# URL : https://atcoder.jp/contests/abc198/tasks/abc198_d

import itertools

S1 = list(input())
S2 = list(input())
S3 = list(input())
num_list = list(range(10))

# 同じ文字は同じindexを割り当てる
num_idx_dict = dict()
S1_idx, S2_idx, S3_idx = [], [], []
now_idx = 0
for char in S1:
    if char in num_idx_dict:
        S1_idx.append(num_idx_dict[char])
    else:
        S1_idx.append(now_idx)
        num_idx_dict[char] = now_idx
        now_idx += 1
        if now_idx == 11:
            print("UNSOLVABLE")
            exit()
for char in S2:
    if char in num_idx_dict:
        S2_idx.append(num_idx_dict[char])
    else:
        S2_idx.append(now_idx)
        num_idx_dict[char] = now_idx
        now_idx += 1
        if now_idx == 11:
            print("UNSOLVABLE")
            exit()
for char in S3:
    if char in num_idx_dict:
        S3_idx.append(num_idx_dict[char])
    else:
        S3_idx.append(now_idx)
        num_idx_dict[char] = now_idx
        now_idx += 1
        if now_idx == 11:
            print("UNSOLVABLE")
            exit()
#print(S1_idx, S2_idx, S3_idx)

flag = False
for pattern in itertools.permutations(num_list):
    # Nの最大桁が0でない
    if pattern[S1_idx[0]] == 0 or pattern[S2_idx[0]] == 0 or pattern[S3_idx[0]] == 0:
        continue
    
    N1, N2, N3 = 0, 0, 0
    p10 = 1
    for digit in range(len(S1_idx)-1, -1, -1):
        N1 += pattern[S1_idx[digit]]*p10
        p10 *= 10
    p10 = 1
    for digit in range(len(S2_idx)-1, -1, -1):
        N2 += pattern[S2_idx[digit]]*p10
        p10 *= 10
    p10 = 1
    for digit in range(len(S3_idx)-1, -1, -1):
        N3 += pattern[S3_idx[digit]]*p10
        p10 *= 10
    
    if N1 + N2 == N3:
        flag = True
        break

if flag:
    print(N1)
    print(N2)
    print(N3)
else:
    print("UNSOLVABLE")