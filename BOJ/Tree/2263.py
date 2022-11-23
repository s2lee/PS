import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def pre_order(post_start, in_start, length):
    if length == 0:
        return

    parent = post_order[post_start + length - 1]
    print(parent, end=" ")

    in_idx = in_dict[parent]
    left = in_idx - in_start
    right = length - left - 1

    pre_order(post_start, in_start, left)
    pre_order(post_start + left, in_start + left + 1, right)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
in_dict = {}
pre_arr = []
for idx, i in enumerate(in_order):
    in_dict[i] = idx

pre_order(0, 0, n)
