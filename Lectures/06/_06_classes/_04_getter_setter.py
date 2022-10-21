class B:
    def __init__(self, x):
        self._x = x

    # getter_1
    def get_x(self):
        return self._x

    # getter_2
    @property
    def x(self):
        return self._x

    # setter_1
    def set_x(self, value):
        self._x = value

    # setter_2
    @x.setter # allows the same name as getter, but different syntax for use 
    def x(self, value):
        self._x = value



b = B(0)

print('1:', b.get_x)
print('2:', b.get_x())
print('3:', b.x)

b.set_x(1)
print('4:', b.x)

b.x = 2
print('5:', b.x)