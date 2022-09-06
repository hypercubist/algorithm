from collections import deque
n = int(input())

# 퀸이 놓여진 위치를 저장할 리스트
q = deque()
result = 0

def dfs(x):
    global result, q
    if x == n:
        result += 1
        return

    for y in range(n):
        if ok(x, y):
            print(x, y)
            q.append((x, y))
            dfs(x+1)
            q.pop()
def ok(x, y):
    global q
    for i in q:
        if x == i[0]:
            return False
        if abs(i[0] - x) == abs(i[1] - y):
            return False
    return True

dfs(0)
print(result)