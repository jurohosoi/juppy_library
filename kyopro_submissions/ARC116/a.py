# URL : https://atcoder.jp/contests/arc116/tasks/arc116_a

T = int(input())
for testcase in range(T):
    N = int(input())
    if N%4 == 0:
        print("Even")
    elif N%2 == 0:
        print("Same")
    else:
        print("Odd")