# keys and rooms

# dfs로 탐색 후 방문하지 않은 방이 있는지 확인, 반복문으로 구현

class Solution:
    def canVisitAllRooms(self, rooms):

        visited = [False] * len(rooms)
        keys = [0]

        while keys:
            room_num = keys.pop()
            if not visited[room_num]:
                visited[room_num] = True
                for key in rooms[room_num]:
                    keys.append(key)

        if False in visited:
            return False
        return True





