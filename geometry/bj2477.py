# 작은 변 2개 = 큰 변 1개
# 큰 사각형 - 작은 사각형
# 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
# 반시계방향 로테이션이므로 방향순서가 동일하다
# 4 2 3 (1 3) 1  -> (1 3)이 작은 사각형
# 방향이 돌아가면 꼭 1, 3이 아닐 수 있다.
# 그러면 큐에 넣어서 뽑다가 같은 수가 두 번 나올 때까지 돌리자

from collections import deque

k = int(input())
arr = []
dir_count = [0] * 6
for _ in range(6):
    dir, dis = map(int, input().split())
    arr.append((dir, dis))
    dir_count[dir] += 1

q = deque(arr)
check = 0
while True:
    item = q.popleft()
    q.append(item)
    if dir_count[item[0]] == 1 and check == 1:
        break
    else:
        check = dir_count[item[0]]

adjusted_arr = list(q)

short_1 = adjusted_arr[1][1]
short_2 = adjusted_arr[2][1]
long_1 = adjusted_arr[4][1]
long_2 = adjusted_arr[5][1]

print((long_1 * long_2 - short_1 * short_2)*k)

