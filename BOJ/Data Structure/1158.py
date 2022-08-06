n, k = map(int, input().split())
circular_list = list(range(1, n + 1))
answer = []
index = 0
while circular_list:
    index = (index + k - 1) % len(circular_list)
    answer.append(str(circular_list.pop(index)))

print(f"<{', '.join(answer)}>")
