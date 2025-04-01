# 30802번 웰컴키트

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
min_b = 0

for i in size:
    if i == 0:
        continue
    if t >= i:
        min_b += 1
    else:
        min_b += (i + t - 1) // t


print(min_b)
print(n//p, n%p)
