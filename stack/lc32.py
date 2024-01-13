# Longest Valid Parentheses

# n이 최대 30000이므로 O(N^2)으로는 힘들다
# 괄호가 열릴 때 스택에 쌓고 닫힐 때 스택을 제거하면서 괄호를 소거시킨다.
# 소거된 위치의 인덱스에 표시를 해서 연결된 표시의 길이 중 최대 길이를 찾는다.


class Solution:

     def longestValidParentheses(self, s):
          arr = list(s)
          open_stack = []
          for i in range(len(s)):
               if s[i] == "(":
                    open_stack.append(i)
               else:
                    if open_stack:
                         open_idx = open_stack.pop()
                         arr[open_idx] = "."
                         arr[i] = "."

          count = 0
          max_count = 0
          for char in arr:
               if char == ".":
                    count += 1
                    max_count = max(max_count, count)
               else:
                    count = 0

          return max_count