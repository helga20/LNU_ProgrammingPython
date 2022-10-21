def decorator(cls):
    
    class Wrapper:
        
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)
        
        def __getattr__(self, name):
            return getattr(self.wrapped, name) * 3

    return Wrapper


@decorator
class A:
    def __init__(self, x, y):
        self.z = 'spam'

a = A(1, 2) # calls Wrapper(1, 2)
print('1:', a.z) # calls Wrapper.__gettatr__(z)