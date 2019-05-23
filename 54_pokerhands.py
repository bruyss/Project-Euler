#! python3
# How many hands does Player 1 win?


class Card(object):
    """Standard playing card"""

    values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, value, suit):
        try:
            self.value = int(value)
        except ValueError:
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

        if self.isflush() and self.isstraight():
            if max(self.cards).value == 14:
                self.handvalue = Hand.handvalue["RoyalFlush"]
                print("Royal flush bb!!!!!")
            else:
                self.handvalue = Hand.handvalue["StraightFlush"]
                self.handscore = max(self.cards).value
        elif self.isflush() and self.handscore < Hand.handvalue["Flush"]:
            self.handvalue = Hand.handvalue["Flush"]
            self.handscore = max(self.cards).value
        elif self.isstraight() and self.handscore < Hand.handvalue["Straight"]:
            self.handvalue = Hand.handvalue["Straight"]
            self.handscore = max(self.cards).value

        if self.handvalue == 0:
            self.handvalue = Hand.handvalue["HighCard"]
            # print("High card")
            mults = [15**x for x in range(5)]
            cardvals = map(lambda x: x.value, self.cards)
            self.handscore += sum({a * b for a, b in zip(cardvals, mults)})

    def __str__(self):
        ret = ""
        for card in self.cards:
            ret += str(card) + " "
        return ret.strip()

    def __eq__(self, other):
        return(
            self.handvalue == other.handvalue
            and self.handscore == other.handscore
        )

    def __gt__(self, other):
        if self.handvalue > other.handvalue:
            return True
        elif self.handvalue == other.handvalue:
            return self.handscore > other.handscore

    def __lt__(self, other):
        if self.handvalue < other.handvalue:
            return True
        elif self.handvalue == other.handvalue:
            return self.handscore < other.handscore

    # def __ge__(self, other):
    #     if self.handvalue >= other.handvalue:
    #         return True
    #     else:
    #         return self.handscore >= other.handscore

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
        return (
            not self.isflush
            and not self.isstraight
            and list(self.vals.values()) in ([1, 1, 1, 2],
                                             [1, 2, 1, 1],
                                             [1, 1, 2, 1],
                                             [2, 1, 1, 1]))

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


with open("54_poker.txt", "r") as f:
    handstext = f.read()

winsP1 = 0
winsP2 = 0
draws = 0
nr = 1

try:
    for line in handstext.split("\n"):
        cardsp1 = []
        cardsp2 = []
        for card in line.split()[:5]:
            cardsp1.append(Card(card[0], card[1]))
        for card in line.split()[5:]:
            cardsp2.append(Card(card[0], card[1]))
        hand1 = Hand(cardsp1)
        hand2 = Hand(cardsp2)
        if hand1 > hand2:
            print(f"{nr}\tWin player 1 ({hand1.handvalue} vs {hand2.handvalue}):\t{str(hand1)}   vs   {str(hand2)}")
            winsP1 += 1
        if hand2 > hand1:
            print(f"{nr}\tWin player 2 ({hand1.handvalue} vs {hand2.handvalue}):\t{str(hand1)}   vs   {str(hand2)}")
            winsP2 += 1
        if hand1 == hand2:
            draw += 1
        nr += 1
except ValueError as ve:
    print(ve)
    pass
finally:
    print(f"Player 1 won {winsP1} games")
    print(f"Player 2 won {winsP2} games")
    print(f"There were {draws} draws")
    print(winsP1 + winsP2 + draws)

# # hand1 = Hand([Card(2, "C"), Card(4, "H"), Card(5, "C"), Card("k", "C"), Card(3, "C")])
# hand2 = Hand([Card(2, "h"), Card(4, "H"), Card(
#     4, "h"), Card("4", "h"), Card(2, "h")])
# # print(str(hand1) + f" {hand1.handvalue} {hand1.handscore}")
# print(str(hand2) + f" {hand2.handvalue} {hand2.handscore}")
