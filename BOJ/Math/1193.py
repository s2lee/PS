x = int(input())
stage, num = 0, 0
while x > num:
    stage += 1
    num += stage

if stage % 2 == 0:
    print(f'{stage - (num - x)}/{(num - x) + 1}')
else:
    print(f'{(num - x) + 1}/{stage - (num - x)}')
