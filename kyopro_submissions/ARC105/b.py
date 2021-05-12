import sys, math
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int,input().split()))

g = 0
for e in A:
    g = math.gcd(g, e)


print(g)