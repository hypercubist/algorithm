def fb(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x > 1:
        return fb(x-2) + fb(x-1)

n = int(input())

print(fb(n))

