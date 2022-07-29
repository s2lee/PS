from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0
queue = deque()
queue.append([0, 0])
while True:
    next_queue = deque()
    flag = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = -1
                    queue.append([nx, ny])
                elif arr[nx][ny] > 0:
                    flag = False
                    arr[nx][ny] += 1
                    if arr[nx][ny] > 2:
                        next_queue.append([nx, ny])
                        arr[nx][ny] = -1

    answer += 1
    queue = next_queue

    if flag:
        break

print(answer - 1)
