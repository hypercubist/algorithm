#LIS

n = int(input())
a = list(map(int, input().split()))
d = [1] * n

#0(n^2) solution
for i in range(1, len(a)):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j]+1)
print(max(d))