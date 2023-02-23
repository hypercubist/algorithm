# 대칭차집합 -> 그림 그려보면 합집합에서 교집합 빼면 된다
# 대칭차 구하는 연산자가 있었다 -> ^

n, m = map(int, input().split())
n_set = set(map(int, input().split()))
m_set = set(map(int, input().split()))

result = n_set ^ m_set
print(len(result))
