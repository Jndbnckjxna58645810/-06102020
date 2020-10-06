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
card1 = Card(rank = "T",suit = Card.SUITS[0])
card2 = Card(rank = "8",suit = Card.SUITS[1]) 
card3 = Card(rank = "3",suit = Card.SUITS[2])
card4 = Card(rank = "10",suit = Card.SUITS[0])
card5 = Card(rank = "D",suit = Card.SUITS[3])    
my_hand = Hand()
my_hand.add(card1) 
my_hand.add(card2)  
my_hand.add(card3)  
my_hand.add(card4)  
my_hand.add(card5) 
print(my_hand)   
your_hand = Hand()
my_hand.give(card1,your_hand)
my_hand.give(card2,your_hand)
print(my_hand)
print(your_hand)
my_hand.clear()
print(my_hand)
deck1 = Deck()
print(deck1)
deck1.populate()
print(deck1)
deck1.shuffle()
print(deck1)
hands = [my_hand,your_hand]
deck1.deal(hands,per_hand = 5)
print(my_hand)
print(your_hand)
print(deck1)
deck1.clear()
