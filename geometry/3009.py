xs = []
ys = []
for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
result = []
if xs[0] == xs[1]:
    result.append(xs[2])
elif xs[1] == xs[2]:
    result.append(xs[0])
else:
    result.append(xs[1])

if ys[0] == ys[1]:
    result.append(ys[2])
elif ys[1] == ys[2]:
    result.append(ys[0])
else:
    result.append(ys[1])

print(result[0], end=" ")
print(result[1])