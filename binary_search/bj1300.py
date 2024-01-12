#

n = int(input())

def smaller_than(x):
    count = 0
    for i in range(1, n + 1):
        count += x // i
    return count

