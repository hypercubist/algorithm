#permutation sequence
import math


#숫자 n개의 숫자로 n자리 순열을 만드는 경우 n!개의 순열이 생성
#k가 어떤 위치에 있는지 찾는게 중요
#n!에서 n부터 나눠가며 앞자리 숫자부터 찾는다


class Solution:
    def getPermutation(self, n, k):
        box = [x for x in range(1, n+1)]
        answer = ""
        def find_next(index):
            count = 0
            result = ""
            for j in range(n):
                if box[j] != -1:
                    count += 1
                    if count == index:
                        result = box[j]
                        box[j] = -1
                        break
            return result

        for i in range(1, n+1):
            idx = 0
            if k == 1:
                idx = 1
            elif k == 2:
                idx = 2
                k = 1
            else:
                chunk = math.factorial(n-i)
                if k % chunk > 0:
                    idx = (k // chunk) + 1
                else:
                    idx = 
                k -= chunk * (idx-1)
            answer += str(find_next(idx))

        return answer

print(Solution.getPermutation("", 4, 9))