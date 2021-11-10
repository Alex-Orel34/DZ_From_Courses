def Erasing(func):
    def check(ls):
        ls=list(filter(lambda x: x % 2 != 0, ls))
        return func(ls)
    return check


@Erasing
def func(ls):
    print(ls)


def main():
    ls=[1,2,3,4,5,8,7,5]
    func(ls)
if __name__=='__main__':
    main()