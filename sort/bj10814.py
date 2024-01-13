import sys
input = sys.stdin.readline

n = int(input())

datas = []
for _ in range(n):
    temp = input().split()
    datas.append((int(temp[0]), temp[1]))

for data in sorted(datas, key= lambda x: x[0]):
    print(data[0], end=" ")
    print(data[1])