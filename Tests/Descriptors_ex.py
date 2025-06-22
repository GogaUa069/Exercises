class A:  # Non-data descriptor
    def __get__(self, instance, owner):
        return ...


class B:  # Data descriptor
    def __get__(self, instance, owner):
        return ...

    def __set__(self, instance, value):
        ...

    def __del__(self):
        ...


# CODE: *************************************************************************


class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) is not int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        setattr(instance, self.name, value)


class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Point3D:
    xr = ReadIntX()
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt = Point3D(1, 2, 3)
print(pt.xr)
pt.xr = 5
print(pt.xr, pt.__dict__)

