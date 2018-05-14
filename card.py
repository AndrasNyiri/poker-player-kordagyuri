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

    def __init__(self, cardCode):
        self.cardCode = cardCode
        self.suit = cardCode[0]
        self.value = self.__card_values[cardCode[1]]

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_card_code(self):
        return self.cardCode
