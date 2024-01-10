# Trapping Rain Water

# 스택에 최근 가장 높은 값을 저장
# 바로 이전 칸 보다 새로 확인 중인 값이 큰 경우..
# 스택 상단(최근 값중 가장 큰 값)과 현재 확인 중인 칸 사이에 있는 값들을 둘 중 작은 값으로 모두 채운다(물 채우기)


class Solution:
    def trap(self, height):
        height_before_rain = height[:]

        now_height = height[0]
        high_stack = [(0, now_height)]
        for i in range(1, len(height)):
            if now_height < height[i]:
                top = high_stack.pop() # 기존 탑스택
                horizon = min(top[1], height[i])
                for j in range(top[0]+1, i):
                    height[j] = max(height[j], horizon)
                if top[1] < height[i]: # 기존 탑스택보다 새로 조회한 값이 클 때 > 새로운 탑
                    high_stack.append((i,height[i]))
                else:
                    high_stack.append(top)
            now_height = height[i]

        return sum(height) - sum(height_before_rain)




