class Deck:
    card_list = []

    def __init__(self, card_list):
        self.card_list = card_list

    def get_ranking(self):
        if self.is_royal_flush():
            return 100

        if self.is_staight_flush():
            return 90

        if self.is_four_of_a_kind():
            return 80

        if self.is_full_house():
            return 70

        if self.is_flush():
            return 60

        if self.is_straight():
            return 50

        if self.is_three_of_a_kind():
            return 40

        if self.is_two_pairs():
            return 30

        if self.is_one_pair():
            return 20

        if self.is_high_card():
            return 10

        return 0

    def is_royal_flush(self):

        return False


    def is_staight_flush(self):
        return False

    def is_four_of_a_kind(self):
        return False

    def is_full_house(self):
        return False

    def is_flush(self):
        result = True
        for i in range(1, len(self.card_list)):
            if self.card_list[0].get_suit() != self.card_list[i].get_suit():
                result = False

        return result

    def is_straight(self):
        return False

    def is_three_of_a_kind(self):
        return False

    def is_two_pairs(self):
        return False

    def is_one_pair(self):
        for i in range(0, len(self.card_list)):
            for j in range(i + 1, len(self.card_list)):
                if self.card_list[i].get_value() == self.card_list[j].get_value():
                    return True
        return False

    def is_high_card(self):
        return True




if __name__ == '__main__':
    Deck()

