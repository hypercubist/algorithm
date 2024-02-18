# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        max_len = 0
        for i in range(n):
            c_set = set([]) # 중복 문자 확인하기 위한 set
            now = i # substring 시작 인덱스
            while now < n:
                if s[now] not in c_set: # 중복 문자 없으면 set에 추가
                    c_set.add(s[now])
                    now += 1
                else:
                    break

            max_len = max(max_len, len(c_set))
        return max_len
