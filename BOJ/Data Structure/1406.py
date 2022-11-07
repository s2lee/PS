import sys

s1 = list(sys.stdin.readline().strip())
s2 = []
m = int(sys.stdin.readline())

for i in range(m):
    com = sys.stdin.readline().strip()
    if com[0] == "P":
        s1.append(com[2])
    elif com[0] == "L" and s1 != []:
        s2.append(s1.pop())
    elif com[0] == "D" and s2 != []:
        s1.append(s2.pop())
    elif com[0] == "B" and s1 != []:
        s1.pop()
print("".join(s1 + list(reversed(s2))))
