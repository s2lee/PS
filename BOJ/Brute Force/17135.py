import sys
from itertools import combinations
from collections import deque

N, M, D = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
board.append([2] * M)


def attack(archer_x, archer_y, kill_set):
    q = deque([(archer_x, archer_y, 0)])
    while q:
        x, y, d = q.popleft()
        if d >= D:
            return
        for dx, dy in (0, -1), (-1, 0), (0, 1):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M or temp_board[nx][ny] == 2:
                continue
            if temp_board[nx][ny] == 1:
                kill_set.add((nx, ny))
                return
            q.append((nx, ny, d + 1))


enemy = sum(line.count(1) for line in board)
answer = 0
for comb in combinations(range(M), 3):
    cnt_killed, archer_row = 0, N
    temp_board = [line[:] for line in board]
    while archer_row > 0:
        kill = set()
        for archer_col in comb:
            attack(archer_row, archer_col, kill)
        for kx, ky in kill:
            temp_board[kx][ky] = 0
            cnt_killed += 1

        archer_row -= 1
        for i in range(M):
            temp_board[archer_row][i] = 2
    answer = max(answer, cnt_killed)

print(answer)
