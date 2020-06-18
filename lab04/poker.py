import random

class Card:
    # card color to unicode symbol dictionary
    unicode_dict = {'s': '\u2660', 'h': '\u2665', 'd': '\u2666', 'c': '\u2663'}
       
    def __init__(self, rank, suit):
    # TODO: define constructor that sets rank and suit of the object.
        pass
    def get_value(self):
    # TODO: method should return a tuple (rank and suit) for example: ('A', 'c')
        pass
    def __str__(self):
    # TODO: should return string: rank of a card and suit. Suit should be unicode symbol rather than 
    # one of the letters 'shdc'. Use unicode_dict for that. 
        pass

class Deck():
    
    def __init__(self, *args):
    # TODO: the constructor should create new deck and assign it to a field. Similar as deck() function from lab02
        pass
    def __str__(self):
    # TODO: define a method that returns a string that consists all of the strings returned by str() method executed on all 
    # the cards. Each card should be separated by space (take a look at lab04.md)
        pass
    def shuffle(self):
    # TODO: shuffle cards
        pass
    def deal(self, players):
    # TODO: deal cards to players, takes list of players as arguments, each player receives card by invoking his take_card() 
    # with card object
        pass

class Player():

    def __init__(self, money, name=""):
        self.__stack_ = money
        self.__name_ = name
        self.__hand_ = []

    def take_card(self, card):
        self.__hand_.append(card)

    def get_stack_amount(self):
        return self.__stack_

    def get_player_hand_immutable(self):
        return tuple(self.__hand_)

    def cards_to_str(self):
    # TODO: returns 
        pass

def histogram(text):
# TODO: put here the method implementation from previous lab
    pass

# dictionary of pairs: card rank string - numerical value. Useful for comparing cards strength
card_rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                    "8": 8, "9": 9, "10": 10, "J": 11, "D": 12,
                    "K": 13, "A": 14}


def get_player_hand_rank(hand):
# TODO: put here the method implementation from previous lab
    pass
 
