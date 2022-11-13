k = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(k)]


def solve(start, end, depth):
    if start > end:
        return
    mid = (start + end) // 2
    tree[depth].append(nums[mid])
    solve(start, mid - 1, depth + 1)
    solve(mid + 1, end, depth + 1)


solve(0, len(nums) - 1, 0)
print("\n".join(" ".join(map(str, t)) for t in tree))