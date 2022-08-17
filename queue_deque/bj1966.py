from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    q = deque()
    for i in range(n):
        q.append((i, data[i]))
    count = 0
    while q:
        p = q.popleft()
        chk = True
        for i in q:
            if p[1] < i[1]:
                chk = False
                break
        if chk:
            count += 1
            if p[0] == m:
                print(count)
                break
        else:
            q.append(p)


