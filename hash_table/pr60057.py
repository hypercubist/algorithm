# 2020 KAKAO BLIND RECRUITMENT 문자열 압축

# 문자를 처음부터 슬라이싱해서 비교
# 첫번째 풀이, 단순 반복 비교
def solution(s):
    answer = len(s)

    for step in range(1, len(s)//2+1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

# 해시맵 이용
def solution(s):
    n = len(s)
    min_len = n
    for step in range(1, len(s)//2 + 1):
        substr = s[:step]
        result = ""
        count = 1
        now = step
        while now + step <= n:
            next = s[now:now+step]
            if substr == next:
                count += 1
            else:
                if count == 1:
                    result += substr
                else:
                    result += str(count) + substr
                count = 1
                substr = next
            now += step

        if count == 1:
            result += substr
        else:
            result += str(count) + substr
        result += s[now:]
        min_len = min(min_len, len(result))

    return min_len


        
