t = int(input())
for _ in range(t):

    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    arr = []
    for i in range(n):
        x, y, r = map(int, input().split())
        arr.append((x, y, r))
    count = 0
    for i in arr:
        x = i[0]
        y = i[1]
        r = i[2]
        if (x - x1)**2 + (y - y1)**2 < r**2 < (x - x2)**2 + (y - y2)**2:
            count += 1
        elif (x - x1)**2 + (y - y1)**2 > r**2 > (x - x2)**2 + (y - y2)**2:
            count += 1

    print(count)