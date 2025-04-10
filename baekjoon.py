x = int(input())

stick = [64, 32, 16, 8, 4, 2, 1]
result = 0
count = 0

for i in stick:
    if x >= i:
        if result + i <= x:
            result += i
            count += 1
    elif result == x:
        break

print(count)