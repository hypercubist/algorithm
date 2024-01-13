# 아마도 계수정렬
# 카운팅할 배열 만들자
arr_count_sg = [0] * 20_000_001

n = int(input())
deck_sg = list(map(int, input().split()))
for card_num in deck_sg:
    arr_count_sg[card_num+10_000_000] += 1 #음수 인덱스는 안되니까 오른쪽으로 밀기

m = int(input())
deck_chk = list(map(int, input().split()))
for card_num in deck_chk:
    if arr_count_sg[card_num+10_000_000] > 0:
        print(1, end=" ")
    else:
        print(0, end=" ")
