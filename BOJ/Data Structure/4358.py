import sys
from collections import Counter
input = sys.stdin.readline

trees = Counter(sys.stdin.read().split("\n"))
del trees[""]
total = sum(trees.values())
for tree, count in sorted(trees.items()):
    print(f"{tree} {100 * count / total:.4f}")
