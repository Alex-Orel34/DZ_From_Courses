import random


class Matrix:
    data = None
    n = None
    m = None

    def __init__(self, n=5, m=5, a=0, b=0):
        if (n is None and m is None) or (a is None and b is None):
            self.data = [[0 for i in range(5)] for j in range(5)]
        else:
            self.m = m
            self.a = a
            self.n = n
            self.b = b
            self.data = [[random.randint(self.a, self.b) for i in range(n)] for j in range(m)]

    def __str__(self):
        string = ''
        for i in self.data:
            for j in i:
                string += '%s\t' % j
            string = string[:-1]
            string += '\n'
        string = string[:-1]
        return string

    def __getitem__(self, idx):
        return self.data[idx]
