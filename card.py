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

    def __init__(self, card_code, is_mine_bool):
        self.card_code = card_code
        self.suit = card_code[0]
        self.value = self.__card_values[card_code[1:]]
        self.is_mine_bool = is_mine_bool

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_card_code(self):
        return self.card_code

    def is_mine(self):
        return self.is_mine_bool
