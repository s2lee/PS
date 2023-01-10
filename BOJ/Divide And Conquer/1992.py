N = int(input())
video = [list(input().strip()) for _ in range(N)]


def quad_tree(v, n, x, y):
    if n == 1:
        return str(v[x][y])

    v1 = quad_tree(v, n // 2, x, y)
    v2 = quad_tree(v, n // 2, x, y + (n // 2))
    v3 = quad_tree(v, n // 2, x + (n // 2), y)
    v4 = quad_tree(v, n // 2, x + (n // 2), y + (n // 2))

    if v1 == v2 == v3 == v4 and len(v1) == 1:
        return v1
    else:
        return f'({v1}{v2}{v3}{v4})'


res = quad_tree(video, N, 0, 0)
print(res)

