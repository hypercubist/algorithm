# n x n 칸의 보드에 n개의 퀸을 놓으려면 각 행, 각 열에 최소 한 개씩은 퀸이 있어야 한다.
# 첫번째 퀸이 놓일 자리를 n개의 케이스로 나누어 생각해볼 수 있을 것 같다.
# 퀸이 갈 수 있는 길은 표시하고 나서 롤백이 번거로우니까 카피해서 값을 넘기는게 좋을 것 같다. -> 시간초과
# 각 행에 대해서 케이스를 나눈 것처럼 각 열에 대해서도 시간을 줄일 방법을 생각 (큐를 이용해볼까)
# 보드에서 놓을 수 없는 자리를 표시하며 갱신하는 것은 시간과 공간 낭비가 크다
# 새로 놓을 퀸과 기존 퀸들의 좌표 관계를 이용하는 것이 좋다.

from collections import deque
n = int(input())

count = 0
set_y = set()
set_xy_m = set()
set_xy_p = set()

# 해당 좌표에 퀸을 놓을 수 있는지 여부 리턴
def possible(x, y):
    if y in set_y:
        return False
    if x-y in set_xy_m:
        return False
    if x+y in set_xy_p:
        return False
    return True


def bt(line):
    global count, set_y, set_xy_m, set_xy_p
    if line == n:
        count += 1
        return
    else:
        for i in range(n):
            if possible(line, i):
                set_y.add(i)
                set_xy_m.add(line - i)
                set_xy_p.add(line + i)
                bt(line + 1)
                set_y.remove(i)
                set_xy_m.remove(line - i)
                set_xy_p.remove(line + i)

bt(0)
print(count)


