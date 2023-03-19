# n^2 정사각배열을 만들어서 채워놓은 다음에 출력해보자
# 모두 1로 채우고 가운데 빈 칸(0)을 뚫어보자

n = int(input())
gh = [[1] * n for _ in range(n)]

def hole(gh, m):
    if m == 1:
        return
    else:
        x = m // 3
        for i in range(len(gh)):
            for j in range(len(gh)):
                if (i // x) % 3 == 1 and (j // x) % 3 == 1:
                    gh[i][j] = 0
        hole(gh, x)

def print_stars(gh, n):
    for i in range(n):
        for j in range(n):
            if gh[i][j] == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

hole(gh, n)
print_stars(gh, n)