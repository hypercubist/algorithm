# 1부터 n개까지 잘라서 집합에 넣기

arr = []
str = input()
n = len(str)
for i in range(1, n+1):
    for j in range(n-i+1):
        arr.append(str[j:j+i])
print(len(set(arr)))