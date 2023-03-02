arr = list(input())
count = [0] * 10
for x in arr:
    count[int(x)] += 1

for i in range(10, 0, -1):
    for _ in range(count[i-1]):
        print(i-1, end="")