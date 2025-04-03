import sys
n = int(input())
n_li = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_li = list(map(int, sys.stdin.readline().split()))
count = 0

dic = {}

for i in n_li:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in m_li:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")

