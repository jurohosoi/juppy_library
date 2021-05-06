# URL : https://atcoder.jp/contests/abc059/tasks/arc072_a

N = int(input())
A = list(map(int, input().split()))

pos_cnt = 0
pos_sum = 0
neg_cnt = 0
neg_sum = 0

for i in range(N):
    if i%2 == 0:
        if pos_sum + A[i] > 0:
            pos_sum += A[i]
        else:
            pos_cnt += 1 - (pos_sum + A[i])
            pos_sum = 1
            
        if neg_sum + A[i] < 0:
            neg_sum += A[i]
        else:
            neg_cnt += (neg_sum + A[i]) - (-1)
            neg_sum = -1
            
    else:
        if neg_sum + A[i] > 0:
            neg_sum += A[i]
        else:
            neg_cnt += 1 - (neg_sum + A[i])
            neg_sum = 1
            
        if pos_sum + A[i] < 0:
            pos_sum += A[i]
        else:
            pos_cnt += (pos_sum + A[i]) - (-1)
            pos_sum = -1
            
print(min(pos_cnt, neg_cnt))