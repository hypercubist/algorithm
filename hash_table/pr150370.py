# 2023 KAKAO BLIND RECRUITMENT 개인정보 수집 유효기간

#


def solution(today, terms, privacies):
    answer = []

    # today int형으로 변경
    today_num = int(''.join(today.split('.')))

    terms_dict = {} # term별 유효기간을 정의할 dict
    for data in terms:
        k, v = data.split(' ')
        terms_dict[k] = v

    index = 0
    for data in privacies:
        index += 1
        agree_date, term = data.split(' ')
        yyyy, mm, dd = agree_date.split('.')
        due = int(terms_dict[term])
        temp_yy = int(yyyy)
        temp_mm = int(mm) + due
        if temp_mm % 12 == 0:
            temp_yy += (temp_mm // 12) - 1
            mm = '12'
        else:
            temp_yy += temp_mm // 12
            if temp_mm % 12 < 10:
                mm = "0"+str(temp_mm % 12)
            else:
                mm = str(temp_mm % 12)

        expire_date = str(temp_yy)+mm+dd
        if int(expire_date) <= today_num:
            answer.append(index)

    return answer