n = int(input())
s_list = {}

for i in range(n):
    s = input()
    for j in range(len(s)):
        if i == 0:
            s_list[j] = s[j]
        if s_list[j] != s[j]:
            s_list[j] = '?'

for value in s_list.values():
    print(value, end='')