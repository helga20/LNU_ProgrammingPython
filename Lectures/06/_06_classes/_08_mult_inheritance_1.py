class C1:
    def method_1(self): self.x = 0
    def method_2(self): print(self.x)

class C2:
    def method_a(self): self.x = 1
    def method_b(self): print(self.x)

class C3(C1, C2): pass # PROBLEM - C3 has only one attribute "x"

item = C3()
item.method_1()
item.method_a()
item.method_2()
item.method_b()
print(item.__dict__)



