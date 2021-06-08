N = int(input())
A = list(map(int, input().split()))

ans = 0
for elt in A:
    ans += max(0, elt - 10)

print(ans)
