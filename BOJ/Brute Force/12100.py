N = int(input())
original_board = [list(map(int, input().split())) for _ in range(N)]


def max_element(matrix):
    result = 0
    for rows in matrix:
        rows.append(result)
        result = max(rows)
    return result


def move_left(matrix):
    result = []
    for rows in matrix:
        new_row = []
        temp = 0
        for num in rows:
            if num == 0:
                continue
            if temp == num:
                new_row[-1] *= 2
                temp = 0
            else:
                new_row.append(num)
                temp = num
        new_row += [0] * (len(rows) - len(new_row))
        result.append(new_row)

    return result


def move_up(matrix):
    result = move_left(list(map(list, zip(*matrix))))
    return list(map(list, zip(*result)))


def move_right(matrix):
    result = []
    for rows in matrix:
        rows.reverse()
        new_row = []
        temp = 0
        for num in rows:
            if num == 0:
                continue
            if temp == num:
                new_row[-1] *= 2
                temp = 0
            else:
                new_row.append(num)
                temp = num
        new_row += [0] * (len(rows) - len(new_row))
        new_row.reverse()
        result.append(new_row)
    return result


def move_down(matrix):
    result = move_right(list(map(list, zip(*matrix))))
    return list(map(list, zip(*result)))


def dfs(board, n):
    global answer
    if n == 5:
        answer = max(answer, max_element(board))
        return
    else:
        dfs(move_left(board), n + 1)
        dfs(move_right(board), n + 1)
        dfs(move_up(board), n + 1)
        dfs(move_down(board), n + 1)


answer = 0
dfs(original_board, 0)
print(answer)
