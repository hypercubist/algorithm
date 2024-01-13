# 가장 기본 단위는 원판이 2개(가장 밑의 큰 원판, 그 위의 원판) 일 때이다.
# 가장 밑의 큰 원판, 그 위의 원판들로 구분, 위의 원판들은 재귀로 돌린다.
# 1 -> 3 으로 옮기는 방법
# 1 -> 2 작은 원판들을 옮긴다(n >= 2, 재귀)
# 1 -> 3 가장 큰 원판 1개를 옮긴다. n = 1
# 2 -> 3 작은 원판들을 큰 원판 위로 옮긴다(n >= 2, 재귀)

trail = []
position = [1, 2, 3]
count = 0
# 2개일 때
def hanoi(n, x, y):
    global count

    if n == 1:
        trail.append((x, y))
        count += 1
    else:
        for z in position:
            if x != z and y != z:
                hanoi(n-1, x, z)
                hanoi(1, x, y)
                hanoi(n-1, z, y)

n = int(input())
hanoi(n, 1, 3)
print(count)
for i in trail:
    print(i[0], end=" ")
    print(i[1])
