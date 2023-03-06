import sys
input = sys.stdin.readline
count = 0


def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

def count_reset():
    global count
    count = 0


t = int(input())

for _ in range(t):
    print(isPalindrome(input().strip()), end = " ")
    print(count)
    count_reset()

