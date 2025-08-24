class ListMath:
    def __init__(self, *args):
        self.lst_math = list()
        if len(args) > 0:
            self.lst_math = [x for x in list(*args) if isinstance(x, (int, float)) and not isinstance(x, bool)]

    def __add__(self, other):  # 1
        return ListMath([i+other for i in self.lst_math])

    def __radd__(self, other):  # 2
        return ListMath([other+i for i in self.lst_math])

    def __iadd__(self, other):  # 3
        return self + other


    def __sub__(self, other):  # 4
        return ListMath([i-other for i in self.lst_math])

    def __rsub__(self, other):  # 5
        return ListMath([other-i for i in self.lst_math])

    def __isub__(self, other):  # 6
        return self - other


    def __mul__(self, other):  # 7
        return ListMath([i*other for i in self.lst_math])

    def __rmul__(self, other):  # 8
        return ListMath([other*i for i in self.lst_math])

    def __imul__(self, other):  # 9
        return self * other


    def __truediv__(self, other):  # 10
        return ListMath([i/other for i in self.lst_math])

    def __rtruediv__(self, other):  # 11
        return ListMath([other/i for i in self.lst_math])

    def __itruediv__(self, other):  # 12
        return self / other
