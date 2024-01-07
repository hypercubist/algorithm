# 2020 KAKAO BLIND RECRUITMENT 자물쇠와 열쇠
import copy


#키를 돌려가며 자물쇠에 꽂아 확인해야함
def solution(key, lock):
    k = len(key)
    l = len(lock)

    # 자물쇠가 움직일 공간을 확보하기 위해 키를 확장
    lock_ext = [[0 for _ in range(l+2*k)] for _ in range(l+2*k)]
    for i in range(l):
        for j in range(l):
            lock_ext[k+i][k+j] = lock[i][j]

    # 키를 확장하고 자물쇠를 움직이는 풀이가 많은 이유이다
    # 자물쇠를 확장하고 키를 움직이게 되면 자물쇠를 별도로 순회해서 채워졌는지 확인해야 한다.
    def is_solved(arr):
        for i in range(k, k+l):
            for j in range(k, k+l):
                if arr[i][j] != 1:
                    return False
        return True

    # 키를 4방향으로 돌려서 각각의 케이스를 keys에 저장
    keys = [[[0 for _ in range(k)] for _ in range(k)] for _ in range(4)]
    for i in range(k):
        for j in range(k):
            keys[0][i][j] = key[i][j]
            keys[1][j][k-1-i] = key[i][j]
            keys[2][k-1-i][k-1-j] = key[i][j]
            keys[3][k-1-j][i] = key[i][j]

    # 4개의 키를 확장된 자물쇠 위에서 위치를 옮겨가며 꽂아본다.
    for now_key in keys:
        for x in range(l+k):
            for y in range(l+k):
                temp_lock = copy.deepcopy(lock_ext)
                for a in range(k):
                    for b in range(k):
                        temp_lock[x+a][y+b] += now_key[a][b]
                if is_solved(temp_lock):
                    return True
                
    # 자물쇠가 열리는 케이스가 없는 경우 잠김으로 표시
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))