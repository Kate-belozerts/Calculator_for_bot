import Logger


def to_complex(operation):
    # result = complex(operation)
    result = eval(operation)  # eval("2 * 0.033e-3 + 1j * 0.12e-3")
    Logger.logger(result, f'complex from {operation}')
    print(result)
    return result


# to_complex("1.5+7j-8+7")
# print(complex(1.5+7j + 5))
# print(int((1.5+7j).real))


#i = -1**0.5 --- корень из -1
#a, b - float
#if b/a == 0 ----- comlex  -> float
# a - действительная часть
# b - мнимая часть с i
# a + bi --- единое число !!!

