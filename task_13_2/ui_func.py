import exception
import classes


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
                print(f'Answer: {classes.Math(a, b).sum()}')
            elif s == '-':
                print('You choose operation -')
                print(f'Answer: {classes.Math(a, b).dif()}')
            elif s == '*':
                print('You choose operation *')
                print(f'Answer: {classes.Math(a, b).mul()}')
            elif s == '/':
                print('You choose operation /')
                print(f'Answer: {classes.Math(a, b).div()}')
        else:
            print('invalid operation sign')
