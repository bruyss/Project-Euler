#! python3
# How many hands does Player 1 win?


class Card(object):
    """Standard playing card"""

    values = {"J": 11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, value, suit):
        try:
            self.value = int(value)
        except ValueError as ve:
            self.value = Card.values(value)
        self.suit = suit

    def __str__(self):
        beeldjes = ["J", "Q", "K", "A"]
        if self.value < 11:
            return str(self.value) + self.suit
        else:
            return beeldjes[self.value - 11] + self.suit

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value
