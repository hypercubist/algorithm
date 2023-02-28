# 프랙탈, 형태에 대해서 일반화해보자

# n = int(input())

def draw(k):
    if k == 1:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    print(" ", end=" ")
                else:
                    print("*", end=" ")
            print()
    else:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    print("", end="")
                else:
                    draw(k-1)
            print()

draw(2)