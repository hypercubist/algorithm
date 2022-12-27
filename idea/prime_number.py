#제곱근 전까지의 모든 수로 나누어 보기 -> 제곱근 이 후는 중복이다.
#이 방법은 에라토스테네스의 체 보다 훨씬 오래걸린다.(중복케이스를 계속해서 점검하므로)
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1): #range는 마지막 숫자는 포함하지 않으므로 +1
        if n % i == 0:
            return False
    return True # 어떤 숫자로도 나누어떨어지지 않았을 때는 소수


#에라토스테네스의 체
import math, time

def get_prime(n):
    if n <= 1:
        return []
    prime = [2] #짝수 중에 유일한 소수
    limit = int(math.sqrt(n))

    data = [i + 1 for i in range(2, n, 2)] #n까지 모든 홀수 리스트

    while limit >= data[0]: #제곱근까지만 계산
        prime.append(data[0])
        data = [j for j in data if j % data[0] != 0] #나누어 떨어지지 않은 수만 살리고 나머지는 제외
    return prime+data