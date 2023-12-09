from collections import Counter
"""Camel Cards modified from https://github.com/rshelswell/projectEuler/poker.py"""

class CamelCard:

    def __init__(self, hand, bid, joker=False):
        self.hand = hand
        self.bid = int(bid.strip())
        self.joker = joker
        if self.joker:
            card_value = dict(zip('J 2 3 4 5 6 7 8 9 T Q K A'.split(), range(14)))
        else:
            card_value = dict(zip('2 3 4 5 6 7 8 9 T J Q K A'.split(), range(14)))

        self.card_values = []

        for card in self.hand:
            self.card_values.append(card_value[card[0]])
        self.ordered_hand = self.card_values.copy()
        self.card_values = sorted(self.card_values)

        # count of values
        self.number_each = Counter(self.card_values)
        self.hierarchy = self.number_each.most_common()
        self.hand_type = self.get_camel_card_hand()

    def __eq__(self, other):
        if not isinstance(other, CamelCard):
            return NotImplemented
        return self.hand == other.hand

    def __lt__(self, other):
        if not isinstance(other, CamelCard):
            return NotImplemented
        elif self == other:
            # equal, so not strictly less than
            return False
        elif self.hand_type < other.hand_type:
            # hand loses
            return True
        elif self.hand_type > other.hand_type:
            # hand wins
            return False
        else:
            # hand types are equal, need to check the card makeup of the hand
            return self.ordered_hand < other.ordered_hand            

    def __str__(self) -> str:
        return f"Hand: {self.hand}\n Bid: {self.bid}\n Type: {self.hand_type}"

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return self == other or self > other

    def get_camel_card_hand(self):

        match self.hierarchy[0][1]:
            # 5 of kind
            case 5:
                return 7
            # 4 of kind
            case 4:
                return 6
            case 3:
                # check full-house
                if self.hierarchy[1][1] == 2:
                    return 5
                else:
                    # 3 of kind
                    return 4
            case 2:
                if self.hierarchy[1][1] == 2:
                    # 2 pair
                    return 3
                else:
                    # pair
                    return 2
            case 1:
                # high card
                return 1
    def get_bid(self):
        return self.bid