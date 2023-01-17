#서로소 집합 알고리즘
#같은 집합의 원소를 찾기
#union연산 : 두 원소가 같은 집합임을 확인하고 연결(루트 노드를 갱신)
#find연산 : 루트 노드를 찾는 연산

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x]) #루트노드가 나올 때까지 재귀탐색
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
