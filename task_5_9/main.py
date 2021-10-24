m, n = list(map(int,input().split()))
for digit in range(m, n+1):
    print(digit,':', end='')
    for denominator in range(2,digit):
        if digit% denominator == 0:
            print(denominator,'',end='')
    print()


