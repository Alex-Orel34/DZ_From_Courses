import math


def Sin1(x,eps):
    y = x
    f = x
    i = 3
    while abs(y) > eps:
        y *= (-1) * x * x / ((i-1)*i)
        i += 2
        f += y
    return f

def main():
    eps = 0.01
    for i in range(0, 6):
        x = math.pi / 4
        print("eps = ", eps, "; sin(", x, ") = ", Sin1(x, eps), ";", math.sin(x))
        eps /= 10




if __name__ == "__main__":
    main()
