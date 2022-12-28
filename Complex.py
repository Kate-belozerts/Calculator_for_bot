import Logger


def to_complex(operation):
    result = eval(operation)
    Logger.logger(result, f'complex from {operation}')
    return result

# to_complex("1.5 + 7j + 7")
# eval("2 * 0.033e-3 + 1j * 0.12e-3")
# print(complex(1.5+7j + 5))
# print(int((1.5+7j).real))
