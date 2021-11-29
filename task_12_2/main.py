import classes


def main():
    ls = [classes.Circle(2, 3, 5), classes.Triangle(3, 4, 5), classes.Square(3, 2)]
    for i in ls:
        print(f'The area of {i} is -- {i.area()};')


if __name__ == '__main__':
    main()
