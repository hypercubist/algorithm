n, m = map(int, input().split())

pool = [x for x in range(1, n+1)]
result = []

def bt(arr):
    if len(arr) == m:
        result.append([x for x in arr]) # arr를 그대로 넘기면 안된다. 값만 넘겨야 함
        return
    for x in pool:
        arr.append(x)
        bt(arr)
        arr.pop()

start = []
bt(start)

for x in result:
    for item in x:
        print(item, end=" ")
    print()
