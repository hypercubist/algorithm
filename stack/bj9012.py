from collections import deque
t = int(input())
ps = []
for _ in range(t):
    ps.append(list(input()))

for i in range(t):
    q = deque()
    result = True
    for j in ps[i]:
        if j == '(':
            q.append(True)
        else:
            try:
                item = q.pop()
            except Exception:
                result = False
                break
    if len(q) > 0:
        result = False
    if result:
        print("YES")
    else:
        print("NO")