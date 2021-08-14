#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/14 14:28
# @Author  : wangjianrong
# @File    : 1.py

import collections
from itertools import product

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchRank:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()  # 花色

    def __init__(self):
        self._cards = [Card(rank, suit) for rank, suit in product(self.ranks, self.suits)]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


if __name__ == '__main__':
    card = Card('8', 'diamonds')
    print(card.rank)
    print(card.suit)
    deck = FrenchRank()
    print(len(deck))
    for item in deck:
        print(item)

