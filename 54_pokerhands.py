#! python3
# How many hands does Player 1 win?


class Card(object):
    """Standard playing card"""

    values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, value, suit):
        try:
            self.value = int(value)
        except ValueError as ve:
            self.value = Card.values[value.upper()]
        self.suit = suit.upper()

    def __str__(self):
        beeldjes = ["T", "J", "Q", "K", "A"]
        if self.value < 10:
            return str(self.value) + self.suit
        else:
            return beeldjes[self.value - 10] + self.suit

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value


class Hand(object):
    """Poker hand of 5 cards"""

    handvalue = {"HighCard": 1, "OnePair": 2, "TwoPairs": 3, "ThreeOfAKind": 4,
                 "Straight": 5, "Flush": 6, "FullHouse": 7,
                 "FourOfAKind": 8, "StraightFlush": 9, "RoyalFlush": 10}

    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError("Hand must contain exactly 5 cards!!")
        self.cards = cards
        self.handvalue = 0
        self.handscore = 0
        self.vals = self.valuedict()

        if self.isflush() and self.isstraight():
            if max(self.cards).value == 14:
                self.handvalue = Hand.handvalue["RoyalFlush"]
                print("Royal flush bb!!!!!")
            else:
                self.handvalue = Hand.handvalue["StraightFlush"]
                self.handscore = max(self.cards).value
        elif self.isflush():
            self.handvalue = Hand.handvalue["Flush"]
            self.handscore = max(self.cards).value
        elif self.isstraight():
            self.handvalue = Hand.handvalue["Straight"]
            self.handscore = max(self.cards).value

        if self.FourOfAKind():
            self.handvalue = Hand.handvalue["FourOfAKind"]
            for value in self.vals:
                if self.vals[value] == 4:
                    self.handscore += value * 15
                else:
                    self.handscore += value

        if self.isfullhouse():
            self.handvalue = Hand.handvalue["FullHouse"]
            for value in self.vals:
                if self.vals[value] == 3:
                    self.handscore += value * 15
                else:
                    self.handscore += value

        if self.ThreeOfAKind():
            self.handvalue = Hand.handvalue["ThreeOfAKind"]
            self.handscore += sum([k for k,
                                   v in self.vals.items() if v == 3]) * 15**2
            singlecards = [k for k, v in self.vals.items() if v == 1]
            singlecards.sort()
            self.handscore += singlecards[0] + singlecards[1] * 15

        if self.twopair():
            self.handvalue = Hand.handvalue["TwoPairs"]
            pairs = [k for k, v in self.vals.items() if v == 2]
            pairs.sort()
            self.handscore += pairs[0] * 15 + pairs[1] * 15**2
            self.handscore += sum([k for k, v in self.vals.items() if v == 1])

        if self.pair():
            self.handvalue = Hand.handvalue["OnePair"]
            self.handscore += sum([k for k,
                                   v in self.vals.items() if v == 2]) * 15**3
            singlecards = [k for k, v in self.vals.items() if v == 1]
            singlecards.sort()
            self.handscore += singlecards[0] + \
                singlecards[1] * 15 + singlecards[2] * 15**2

        if self.handvalue == 0:
            self.handvalue = Hand.handvalue["HighCard"]
            mults = [15**x for x in range(5)]

    def __str__(self):
        return " ".join(self.cards)

    def isflush(self):
        return all([self.cards[0].suit == c.suit for c in self.cards])

    def isstraight(self):
        cardset = set(
            map(lambda x: x.value - min(self.cards).value, self.cards))
        return cardset == set(range(5))

    def valuedict(self):
        vals = {}
        for card in self.cards:
            vals[card.value] = vals.get(card.value, 0) + 1
        return vals

    def isfullhouse(self):
        return set(self.vals.values()) == {3, 2}

    def pair(self):
        return list(self.vals.values()) in ([1, 1, 1, 2],
                                            [1, 2, 1, 1],
                                            [1, 1, 2, 1],
                                            [2, 1, 1, 1])

    def twopair(self):
        return (
            self.handvalue < Hand.handvalue["TwoPairs"]
            and list(self.vals.values()) in ([2, 2, 1], [2, 1, 2], [1, 2, 2])
        )

    def ThreeOfAKind(self):
        return (
            self.handvalue < Hand.handvalue["ThreeOfAKind"]
            and list(self.vals.values()) in ([3, 1, 1], [1, 3, 1], [1, 1, 3])
        )

    def FourOfAKind(self):
        return list(self.vals.values()) in ([4, 1], [1, 4])


