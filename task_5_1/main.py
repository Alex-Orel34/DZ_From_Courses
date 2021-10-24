while True:
    sign = input("Sing (+,-,*,/): ")
    if sign == '0':
        break
    if sign in ('+', '-', '*', '/'):
        X, Y = list(map(float, input('Put X and Y').split()))
        if sign == '+':
            print(f'Result of sum is:{X + Y}')
        elif sign == '-':
            print(f' Result of difference is:{X - Y}')
        elif sign == '*':
            print(f'Result of multiplication is: {X * Y}')
        elif sign == '/':
            if Y != 0:
                print(f'Result of division is: {(X / Y)}')
            else:
                print("Division by zero!")
    else:
        print("Put correct sign")
