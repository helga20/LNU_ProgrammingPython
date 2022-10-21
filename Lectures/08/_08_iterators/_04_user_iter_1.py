class DiceImitator:

    def __init__(self, limit):
        from random import randint
        self.randint = randint
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.randint(1, 6)
        raise StopIteration

    def __iter__(self): # is needed for use with "for"
        return self


game1 = DiceImitator(3)
game2 = DiceImitator(3)

print('\nGame 1')
for i in game2:
    print('1:', i)

print('\nGame 2')
while True:
    print('2:', next(game1))

