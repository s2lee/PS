import sys

order = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
sentence = list(sys.stdin.readline().rstrip())
oper_stack = []

for sign in sentence:
    if sign.isalpha():
        print(sign, end="")

    elif sign == "(":
        oper_stack.append(sign)

    elif sign == ")":
        while oper_stack[-1] != "(":
            print(oper_stack.pop(), end="")
        oper_stack.pop()

    else:
        while oper_stack and order[oper_stack[-1]] >= order[sign]:
            print(oper_stack.pop(), end="")

        oper_stack.append(sign)

print(*reversed(oper_stack), sep="")
