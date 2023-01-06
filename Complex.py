import Logger


def to_complex(operation):
    operation = operation.replace(' ', '')
    z1 = ''
    z2 = ''
    if '=' in operation:
        a = operation.index('=')
        b = operation[a:].index('z')
        size = operation[a+1:b]
        for i in range(len(size)):
            z1 += size[i]
        sign = operation[b]
        z1 = complex(z1)

        size = operation[b+3:]
        for j in range(len(size)):
            z2 += size[j]
        z2 = complex(z2)

    else:
        a = operation.index('j')
        size = operation[:a+1]
        for i in range(len(size)):
            z1 += size[i]
        z1 = complex(z1)
        sign = operation[a+1]

        size = operation[a+2:]
        for j in range(len(size)):
            z2 += size[j]
        z2 = complex(z2)

    if sign == '+':
        result = z1 + z2
    if sign == '-':
        result = z1 - z2
    if sign == '/':
        result = z1 / z2
    if sign == '*':
        result = z1 * z2

    Logger.logger(result, f'complex from {operation}')
    return result


# o = 'z = 2+5j + z = 3 - 3j'
# b = '2 + 5j - 6 - 3j'
# to_complex(b)





#a, b - float
#if b/a == 0 ----- comlex  -> float
# a - действительная часть
# b - мнимая часть с i
# a + bi --- единое число
#i = -1**0.5 --- корень из -1
# print(int((1.5+7j).real))
