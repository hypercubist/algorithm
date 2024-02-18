# 2021 KAKAO BLIND RECRUITMENT 신규 아이디 추천

# 단계별로 일단 진행
# 시간초과 안남
def solution(new_id):

    # step1 소문자로 치환
    step1 = new_id.lower()

    # step2 허용되지 않는 특수문자 제거
    step2 = ""
    for x in step1:
        if x.isalpha() or x.isdigit():
            step2 += x
        elif x in {"-", "_", "."}:
            step2 += x

    # step3 연속된 마침표 제거
    step3 = ""
    for x in step2:
        if x == ".":
            if len(step3) > 0 and step3[-1] == ".":
                continue
            else:
                step3 += x
        else:
            step3 += x

    # step4 처음과 마지막 위치 마침표 제거
    temp = step3
    if len(temp) > 0 and temp[0] == ".":
        temp = temp[1:]
    if len(temp) > 0 and temp[-1] == ".":
        temp = temp[:-1]
    step4 = temp

    # step5 빈문자열 체크
    step5 = step4
    if step5 == "":
        step5 = "a"

    # step6 최대 길이 제한
    step6 = step5
    if len(step6) >= 16:
        step6 = step6[:15]
        if step6[-1] == ".":
            step6 = step6[:-1]

    # step7 최소 길이 제한
    step7 = step6
    if len(step7) <= 2:
        while len(step7) < 3:
            step7 += step7[-1]

    return step7