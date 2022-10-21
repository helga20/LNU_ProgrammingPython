import time

class Cycling:

    def __init__(self, list_):
        self.list = list_
        self.index = 0

    def __next__(self):
        value_to_return = self.list[self.index]
        if self.index == len(self.list) - 1:
            self.index = 0
        else:
            self.index += 1
        return value_to_return

    def __iter__(self):
        return self


colors = Cycling(['red', 'yellow', 'green'])
for i in colors:
    print(i)
    time.sleep(2) 