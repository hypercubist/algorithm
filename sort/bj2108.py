import sys
input = sys.stdin.readline

n = int(input())
arr = []
count = [0] * 8001
for _ in range(n):
    x = int(input())
    arr.append(x)
    count[x+4000] += 1
total = sum(arr)
max_count = max(count)
max_idx_list = []
max_idx = 0
for i in range(len(count)):
    if count[i] == max_count :
        max_idx_list.append(i)

if len(max_idx_list) > 1:
    max_idx = sorted(max_idx_list)[1]
else:
    max_idx = max_idx_list[0]
max = max(arr)
min = min(arr)
result1 = total / n
result2 = sorted(arr)[n//2]
result3 = max_idx - 4000
result4 = max - min

if "%0.0f"%result1 == "-0":
    print("0")
else:
    print("%0.0f"%result1)
print(result2)
print(result3)
print(result4)
