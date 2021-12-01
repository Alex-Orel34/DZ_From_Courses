import exception
import func


def get_number():
    while True:
        number = input()
        if number.isdigit():
            return int(number)
        else:
            raise exception.MyException


def Process():
    while True:
        s = input("Sign (+,-,*,/): \n")
        if s == '0':
            break
        if s in ('+', '-', '*', '/'):
            print('Enter numbers')
            a = get_number()
            b = get_number()
            if s == '+':
                print('You choose operation +')
                print(f'Answer: {func.summa(a, b)}')
            elif s == '-':
                print('You choose operation -')
                print(f'Answer: {func.dif(a, b)}')
            elif s == '*':
                print('You choose operation *')
                print(f'Answer: {func.mul(a, b)}')
            elif s == '/':
                print('You choose operation /')
                print(f'Answer: {func.div(a, b)}')
        else:
            print('invalid operation sign')
