t = int(input())
nf, rf = 1, 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

for i in range(t):
    n, m = map(int, input().split())
    print(int(factorial(m) / (factorial(m-n) * factorial(n))))