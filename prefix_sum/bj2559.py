n, k = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = []
sum = sum(numbers[0:k])
prefix_sum.append(sum)
for i in range(1, n-k+1):
    sum = sum - numbers[i-1] + numbers[i+k-1]
    prefix_sum.append(sum)

print(max(prefix_sum))
