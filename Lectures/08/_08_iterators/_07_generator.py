def dice_imitator(limit):
    from random import randint
    for _ in range(limit):
        yield randint(1, 6)
       

game1 = dice_imitator(3)
game2 = dice_imitator(3)

print('\nGame 1')
for i in game2:
    print('1:', i)

print('\nGame 2')
while True:
    print('2:', next(game1))

