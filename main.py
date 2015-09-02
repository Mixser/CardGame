from enum import Enum

Suit = Enum('hearts', 'titles', 'clovers', 'pikes')

rank = ['one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']

Rank = Enum(*rank)


class Card(object):
    def __init__(self, suit, rank):
        if suit not in Suit or rank not in Rank:
            raise ValueError
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return '<Card: %s %s>' %(self.suit, self.rank)


class Player(object):
    def __init__(self):
        self._name = 'unknown'
        self._cards = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def add_card(self, *args):
        self._cards.extend(args)


if __name__ == '__main__':
    c = Card(Suit.hearts, Rank.one)
    u = Player()


