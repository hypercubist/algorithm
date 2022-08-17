import sys
input = sys.stdin.readline
n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key= lambda x:(x[1], x[0]))

end, count = 0, 0

for i in range(n):
    if meeting[i][0] >= end:
        count +=1
        end = meeting[i][1]
print(count)