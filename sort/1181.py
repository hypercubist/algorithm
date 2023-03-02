import sys
input = sys.stdin.readline

n = int(input())
datas = []
for _ in range(n):
    data = input().strip()
    # datas.append((len(data), data))
    datas.append(data)
sorted_datas = sorted(datas, key= lambda x: (len(x), x))

temp = ""
for x in sorted_datas:
    if x != temp:
        temp = x
        print(x)
