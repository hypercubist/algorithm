import copy
n, m = map(int, input().split())

pool = [x for x in range(1, n+1)] # [1,2,3,4]
result = []
small = []
def bt(small, depth):
    if depth == m: # 종료조건
        result.append(copy.deepcopy(small))
    else:
        for x in pool:
            if x not in small:
                small.append(x)
                bt(small, depth+1)
                small.pop()
bt(small, 0)

for x in result:
    for y in x:
        print(y, end=" ")
    print()