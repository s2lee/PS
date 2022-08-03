import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = [[0, []] for _ in range(N + 1)]
for i in range(2, N + 1):
    animal, animal_cnt, island = input().split()
    if animal == 'W':
        animal_cnt = -int(animal_cnt)
    graph[i][0] = int(animal_cnt)
    graph[int(island)][1].append(i)


def dfs(depth):
    answer = graph[depth][0]
    for x in graph[depth][1]:
        answer += dfs(x)

    if answer < 0:
        return 0
    else:
        return answer


print(dfs(1))
