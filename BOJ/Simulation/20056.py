from collections import deque, defaultdict
import math
import sys

input = sys.stdin.readline


def check_all_even_or_odd(array):
    a = [x for x in array if x % 2 == 0]
    b = [x for x in array if x % 2 == 1]
    if len(a) == len(array) or len(b) == len(array):
        return True
    return False


n, m, k = map(int, input().split())
q = deque()
for _ in range(m):
    q.append(list(map(int, input().split())))

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
cnt = 0
while cnt < k:
    new_q = deque()
    v_dict = defaultdict(list)

    # 이동
    for _ in range(len(q)):
        r, c, m, s, d = q.popleft()
        next_r, next_c = (r + dr[d] * s) % n, (c + dc[d] * s) % n
        v_dict[(next_r, next_c)].append([m, s, d])

    # 2개 이상 파이어볼 있는 칸 찾아서 분화 후 큐에 넣기
    for key in v_dict:
        r, c = key
        if len(v_dict[key]) > 1:
            m_sum_value, s_sum_value, d_list = 0, 0, []
            for x in v_dict[key]:
                m, s, d = x
                m_sum_value += m
                s_sum_value += s
                d_list.append(d)

            m_sum_value = math.floor(m_sum_value / 5)
            s_sum_value = math.floor(s_sum_value / len(v_dict[key]))
            if m_sum_value == 0:
                continue

            if check_all_even_or_odd(d_list):
                for i in range(0, 7, 2):
                    new_q.append([r, c, m_sum_value, s_sum_value, i])
            else:
                for i in range(1, 8, 2):
                    new_q.append([r, c, m_sum_value, s_sum_value, i])
        else:
            m, s, d = v_dict[key][0]
            new_q.append([r, c, m, s, d])

    q = new_q
    cnt += 1

ans = sum(x[2] for x in q)
print(ans)
