#131.Palindrome Partitioning


class Solution:
    def partition(self, s):
        output = []

        def is_palindrome(word):
            s = 0
            e = len(word) - 1
            result = True
            while s <= e:
                if word[s] != word[e]:
                    result = False
                    break
                s += 1
                e -= 1
            return result

        def bt(word, combi, now):
            if now == len(word):
                output.append(combi[:])
                return
            start = now
            while now <= len(word): # 아래 로직에서 슬라이싱하면서 [start:end]에서 end는 포함되지 않으므로 now = len(word)케이스가까지 확인해야한다.
                now += 1
                if is_palindrome(word[start:now]):
                    combi.append(word[start:now])
                    bt(word, combi, now)
                    combi.pop()

        combi_box = []
        bt(s, combi_box, 0)
        return output


