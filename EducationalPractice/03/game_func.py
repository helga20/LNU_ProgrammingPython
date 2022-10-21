from player_func import *
class Game:
    def __init__(self, player1, player2, table = []):
        self.player1 = player1
        self.player2 = player2
        self.table = table

    def print_on(self):
        print(f"STATE: Player 1: {self.player1.get_cards()}"
            f"--- Player 2: {self.player2.get_cards()}"
            f" --- Table: {self.table}")

    def table_upper_identical(self, player):
        if len(self.table) and len(player.get_cards()):
            t = self.table[len(self.table)-1]
            return player.put_card() == t
        return False

    def start(self):
        self.print_on()
        while len(self.player1.get_cards()) and len(self.player2.get_cards()):
            print(f"Player 1 put: {self.player1.put_card()}")
            if self.table_upper_identical(self.player1):
                self.player2.take_card(self.player1.put_card())
                print(f"Player 2 take: ", self.player1.cards.pop())
            else:
                self.table.append(self.player1.cards.pop())
            self.print_on()
            print(f"Player 2 put: {self.player2.put_card()}")
            if self.table_upper_identical(self.player2):
                self.player1.take_card(self.player2.put_card())
                print(f"Player 1 take: ", self.player2.cards.pop())
            else:
                self.table.append(self.player2.cards.pop())
            self.print_on()
        for i in range(len(self.table)-3):
            if self.table[i]%2 !=0 and self.table[i+1]%2 !=0\
                and self.table[i+2]%2 !=0:
                print ("GAME END!") 
            break
        if sum(self.table)%2 != 0:
             print("Winer: Player 2") 
        else:
            print("Winer: Player 1")
