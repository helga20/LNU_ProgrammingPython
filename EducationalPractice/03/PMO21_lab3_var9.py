from player_func import *
from game_func import *

player_1 = Player()
player_1.create_card()
player_2 = Player()
player_2.create_card()
game = Game(player_1, player_2)
game.start()
