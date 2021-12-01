import exception


def summa(a, b):
    return a + b


def dif(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except exception.MyException :
        print(f'Denominator is Zero')
