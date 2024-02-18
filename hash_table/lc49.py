# 49. Group Anagrams

# anagram은 문자열의 문자 구성과 갯수가 같은 여러 문자열들
# 문자열 구성과 갯수를 묶어서 set에 담고 같은 set인 경우 anagram이라고 볼 수 있다

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anagram_dd = defaultdict(list)
        for string in strs:
            dd = defaultdict(int)
            for c in string:
                dd[c] += 1

            key_str = ""
            for k, v in sorted(dd.items()):
                print(k, v)
                key_str += k+str(v)
            anagram_dd[key_str].append(string)

        return anagram_dd.values()



