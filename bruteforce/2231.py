# 1부터 올라가다가 찾으면 멈추자

n = int(input())

result = 0
for i in range(1, n+1):
    arr = list(str(i))
    d = len(arr)
    dsum = 0
    for j in range(d):
        dsum += int(arr[j]) + (int(arr[j]) * (10**(d-1-j)))
    if dsum == n:
        result = i
        break
print(result)