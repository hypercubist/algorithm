import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# a = [] 그냥 배열에 담으니까 n^2으로 시간초과된다
# 아마도 딕셔너리로 검색해야할 듯?

x = {}
y = []
q = []

for i in range(n):
    a = input().strip() ## readline으로 입력 받는 경우 개행문자까지 가져오므로 잘라내고 넣어준다.
    x[a] = i
    y.append(a)

for _ in range(m):
    q.append(input().strip())

for item in q:
    result = ""
    try:
        result = y[int(item)-1]
    except ValueError:
        result = x[item]+1
    finally:
        print(result)
