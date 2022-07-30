from collections import deque
import sys


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1] * n for _ in range(n)]
ocean = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
island_num = 2


def numbering(x, y, num):
    q = deque([(x, y)])
    graph[x][y] = num
    distance[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = num
                    distance[nx][ny] = 0
                    q.append((nx, ny))
                elif graph[nx][ny] == 0:
                    ocean.append((x, y, num))


def extend():
    flag = False
    answer = sys.maxsize
    while ocean:
        size = len(ocean)
        for _ in range(size):
            x, y, num = ocean.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = num
                        distance[nx][ny] = distance[x][y] + 1
                        ocean.append((nx, ny, num))
                    elif graph[nx][ny] != num:
                        answer = min(answer, distance[x][y] + distance[nx][ny])
                        flag = True
        if flag:
            print(answer)
            return


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            numbering(i, j, island_num)
            island_num += 1

extend()
