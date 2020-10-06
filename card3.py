import random
class Card:
    """1 Card"""
    RANKS = ["T","2","3","4","5","6","7","8","9","10","B","D","K"]
    SUITS = [u'\u2660',u'\u2663',u'\u2665',u'\u2666']
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep
class Hand:
    """HAND"""
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "0"
        return rep
    def clear(self):
        self.cards = []
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)
class Unprintable_Card(Card):
    """DO NOT SHOW"""
    def __str__(self):
        return("can not print")
class Positionable_Card(Card):
    def __init__(self,rank,suit,face_up = True):
        super().__init__(rank,suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = "XX"
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up
class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self,hands,per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("No cards left")
a = random.randint(0,14)
if a == 0 or a == 14:
    r = '2'
elif a == 1:
    r = '3'
elif a == 2:
    r = '4'
elif a == 3:
    r = '5'
elif a == 4:
    r = '6'
elif a == 5:
    r = '7'
elif a == 6:
    r = '8'
elif a == 7:
    r = '9'
elif a == 8:
    r = '10'
elif a == 9:
    r = 'B'
elif a == 10:
    r = 'D'
elif a == 11:
    r = 'K'
elif a == 12 or a == 13:
    r = 'T'
s = random.randint(0,4)
c1 = Unprintable_Card(r,Card.SUITS[s])
a = random.randint(0,14)
if a == 0 or a == 14:
    r = '2'
elif a == 1:
    r = '3'
elif a == 2:
    r = '4'
elif a == 3:
    r = '5'
elif a == 4:
    r = '6'
elif a == 5:
    r = '7'
elif a == 6:
    r = '8'
elif a == 7:
    r = '9'
elif a == 8:
    r = '10'
elif a == 9:
    r = 'B'
elif a == 10:
    r = 'D'
elif a == 11:
    r = 'K'
elif a == 12 or a == 13:
    r = 'T'
s = random.randint(0,4)
c2 = Positionable_Card(r,Card.SUITS[s])
print(c1)
print(c2)
c2.flip()
print(c2)