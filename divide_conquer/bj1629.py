import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())

def divide(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (divide(a, b//2, c) ** 2) % c
    else:
        return ((divide(a, b//2, c) ** 2) * a) % c

print(divide(a, b, c))