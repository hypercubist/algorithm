#decimal to binary
n = 31
result = ''
while n > 0:
    result = str(n % 2) + result #나머지를 문자열의 왼쪽에 붙임 -> 숫자로 더하지 않고 문자열로 다루는 방식이 재밌다
    n //= 2 #2로 나눈 몫을 다시 대입
print(result)

#binary to decimal
n = '10010'
result = 0
for i in range(len(n)):
    result += int(n[i]) * (2 ** (len(n) - i - 1))
print(result)