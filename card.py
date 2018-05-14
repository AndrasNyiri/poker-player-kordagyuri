class Card:

    __card_values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def __init__(self, suit, rank, is_mine_bool):
        self.suit = suit
        self.value = self.__card_values[rank]
        self.is_mine_bool = is_mine_bool

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def is_mine(self):
        return self.is_mine_bool
