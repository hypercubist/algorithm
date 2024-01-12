# 괄호는 한 쌍이니까 해시테이블 사용 > 하지만 괄호 종류의 갯수가 적어 속도상 큰 이점이 있을 것이라고 생각되지는 않음..
# 괄호를 열기만 하고 끝나는 문자열의 경우 스택에 데이터가 남아있게 되는데 이 경우를 체크하지 않아서 오답
# 스택을 사용해야할 것 같다

class Solution:
    def isValid(self, s):

        ht = {")": "(", "}": "{", "]": "["}
        p_stack = []
        for c in s:
            if c in ht:
                if len(p_stack) > 0:
                    if ht[c] != p_stack.pop():
                        return False
                else:
                    return False
            else:
                p_stack.append(c)

        if len(p_stack) > 0:
            return False
        return True

