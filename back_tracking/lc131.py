#131.Palindrome Partitioning

#



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

        def bt(word, start, end, arr):
            if end > len(word)-1:
                output.append(arr)
                return
            end += 1
            if is_palindrome(word[start:end]):






