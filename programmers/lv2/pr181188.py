targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

points = [0] * 10_000_000

for m in targets:
    for i in m:
        points[i] += 1

while 