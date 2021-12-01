class Math:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def sum(self):
        return self._a + self._b

    def dif(self):
        return self._a - self._b

    def mul(self):
        return self._a * self._b

    def div(self):
        try:
            return self._a / self._b
        except ZeroDivisionError as err:
            print(f'Denominator is Zero {err}')
