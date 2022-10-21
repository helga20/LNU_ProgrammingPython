from random import randint as rn

class Player:
    def __init__(self, cards = []):
        self.cards = cards
        
    def create_card(self):
        self.cards = [rn(1, 9) for i in range(5)]

    def get_cards(self):
        return self.cards
    
    def put_card(self):
        return self.cards[len(self.cards)-1]

    def take_card(self, card):
        self.cards.insert(0, card)
