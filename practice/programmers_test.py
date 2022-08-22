import copy
def flip_row(k, gh):
    for i in range(len(gh[0])):
        if gh[k][i] == 0:
            gh[k][i] = 1
        else:
            gh[k][i] = 0

def flip_col(k, gh):
    for i in range(len(gh)):
        if gh[i][k] == 0:
            gh[i][k] = 1
        else:
            gh[i][k] = 0

def chk(gh1, gh2):
    for i in range(len(gh1)):
        for j in range(len(gh1[0])):
            if gh1[i][j] != gh2[i][j]:
                return False
    return True

def row_first(arr, target):
    answer = 0
    temp = copy.deepcopy(arr)
    for i in range(len(temp)):
        if temp[i][0] != target[i][0]:
            flip_row(i, temp)
            answer += 1
    for i in range(len(temp[0])):
        if temp[0][i] != target[0][i]:
            flip_col(i, temp)
            answer += 1
    if chk(temp, target):
        return answer
    else:
        return -1

def col_first(arr, target):
    answer = 0
    temp = copy.deepcopy(arr)
    for i in range(len(temp[0])):
        if temp[0][i] != target[0][i]:
            flip_col(i, temp)
            answer += 1
    for i in range(len(temp)):
        if temp[i][0] != target[i][0]:
            flip_row(i, temp)
            answer += 1
    if chk(temp, target):
        return answer
    else:
        return -1

def solution(beginning, target):
    answer1 = row_first(beginning, target)
    answer2 = col_first(beginning, target)
    flip_row(0, beginning)
    answer3 = row_first(beginning, target)
    answer4 = col_first(beginning, target)
    return min(answer1, answer2, answer3+1, answer4+1)


