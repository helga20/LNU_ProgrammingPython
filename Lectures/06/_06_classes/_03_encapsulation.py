# NO REALLY ENCAPSULATION IN PYTHON - ALL IS PUBLIC!

class A:
    def __init__(self, x, y, z):
        self.x = x # public
        self._y = y # declaratively private
        self.__z = z # pseudo private

a = A(1, 2, 3)

print('1:', a.x)

#print('2:', a.y)
print('3:', a._y)

#print('4:', a.__z)
print('5:', a._A__z)

print('6:', a.__dict__)
 
