s = input().rstrip('\n')
array = []
try:
    for i in s:
        if i == ')':
            k = 0
            while array[-1] != '(':
                k += array.pop()
            array.pop()
            if k:
                array.append(k * 2)
            else:
                array.append(2)
        elif i == ']':
            k = 0
            while array[-1] != '[':
                k += array.pop()
            array.pop()
            if k:
                array.append(k * 3)
            else:
                array.append(3)
        else:
            array.append(i)

    print(sum(array))
except:
    print(0)

