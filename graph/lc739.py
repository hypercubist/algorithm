# daily temperatures

# 더 따뜻한 날을 찾기 위해서 리스트를 순회하는 경우 시간복잡도는 O(N^2)이 될 것이다.
# 리스트의 길이가 10^5이므로 N^2로는 시간초과가 예상된다.

# 리스트 순회 중 스택에 온도와 날짜 인덱스를 저장할 것
# 새로 스택에 넣을 온도가 기존 스택에 있는 온도보다 높은 경우 모두 pop하고 경과일(인덱스 차이)를 기록한다.
class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0 for _ in range(len(temperatures))]
        temp_stack = []
        now = 101 # 처음에 스택을 쌓기 위해서 가능한 온도보다 높게 설정
        for i, temp in enumerate(temperatures):
            if now < temp:
                while temp_stack:
                    pop_data = temp_stack.pop()
                    if pop_data[0] < temp:
                        result[pop_data[1]] = i - pop_data[1]
                    else:
                        temp_stack.append(pop_data)
                        break
            temp_stack.append((temp, i))
            now = temp

        return result
