n = int(input())
k = int(input())

# 2차원 배열 내에서 x보다 작거나 같은 수의 갯수
# 이 리턴된 갯수가 k보다 크거나 같은 경우는 답이 될 수 있는 케이스이다.
# 이 리턴된 갯수가 k보다 작은 경우는 답이 될 수 없는 케이스이다.
def count_smaller_than(x):
    count = 0
    for i in range(1, n+1):
        count += min(x//i, n)
    return count

def bin(t, s, e):
    result = -1
    while s < e:
        x = (s + e) // 2
        if t <= count_smaller_than(x):
            e = x
            result = x
        else:
            s = x + 1
    return result

print(bin(k, 1, k))
