import classes
import func


def main():
    a = classes.Matrix()
    print('Our Matrix:')
    print(a)
    print(f'Matrix max element is {func.max_elem(a)}')
    print(f'Matrix min element is {func.min_elem(a)}')


if __name__ == '__main__':
    main()
