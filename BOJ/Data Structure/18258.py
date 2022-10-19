from collections import deque
import sys

q = deque()
for _ in range(int(input())):
    cmd, *num = sys.stdin.readline().split()
    if cmd == 'push':
        q.append(num[0])
    elif cmd == 'pop':
        print(q.popleft() if q else -1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        print(0 if q else 1)
    elif cmd == 'front':
        print(q[0] if q else -1)
    elif cmd == 'back':
        print(q[-1] if q else -1)
