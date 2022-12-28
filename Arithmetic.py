import Logger


def addition(operation):
    operation = operation.split('+')
    result = float(operation[0]) + float(operation[1])
    if result % 1 == 0:
        result = int(result)
    Logger.logger(result, 'result of addition')
    return result


def subtract(operation):
    operation = operation.split('-')
    result = float(operation[0]) - float(operation[1])
    if result % 1 == 0:
        result = int(result)
    Logger.logger(result, 'result of subtract')
    return result


def division(operation):
    operation = operation.split('/')
    result = float(operation[0]) / float(operation[1])
    if result % 1 == 0:
        result = int(result)
    Logger.logger(result, 'result of division')
    return result


def multiply(operation):
    operation = operation.split('*')
    result = float(operation[0]) * float(operation[1])
    if result % 1 == 0:
        result = int(result)
    Logger.logger(result, 'result of multiply')
    return result


def exponent(operation):
    operation = operation.split('^')
    result = float(operation[0]) ** float(operation[1])
    if result % 1 == 0:
        result = int(result)
    Logger.logger(result, 'result of exponent')
    return result


def root(operation):
    operation = operation.split('root')
    result = float(operation[0]) ** 0.5
    Logger.logger(result, 'the root of the number is')
    return result
