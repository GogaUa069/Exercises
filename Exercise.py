from math import sqrt


class Complex:
    """
    Working with complex numbers
    """
    def __init__(self, real, img):
        """
        :param real: int/float. Real part of complex number.
        :param img: int/float. Imaginary part of complex number.
        """
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if type(value) in (int, float):
            self.__real = value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if type(value) in (int, float):
            self.__img = value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        """
        :return: The square root of the sum of the squares of the real and imaginary parts of a complex number.
        """
        return sqrt(self.real**2 + self.__img**2)


# EX. <<<
#cmp = Complex(7, 8)
#cmp.real = 3
#cmp.img = 4
#c_abs = abs(cmp)
#print(cmp.real, cmp.img, c_abs)
