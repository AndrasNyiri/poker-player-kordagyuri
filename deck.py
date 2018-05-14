from card import Card


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
        if self.is_flush() and self.is_straight():
            return True
        else:
            return False

    def is_staight_flush(self):
        return False

    def is_four_of_a_kind(self):
        value = 0
        for i in range(len(self.card_list)):
            same_count = 0
            for j in range(len(self.card_list)):
                if self.card_list[i].get_value() == self.card_list[j].get_value():
                    same_count += 1
                    value += self.card_list[j].get_value()
            if same_count == 4:
                return value
        return 0

    def is_full_house(self):
        return False

    def is_flush(self):
        value = 0
        count = 0
        for i in range(len(self.card_list)):
            if self.card_list[0].get_suit() == self.card_list[i].get_suit():
                value += self.card_list[i].get_value()
                count += 1

        if count == 5:
            return value
        return 0

    def is_straight(self):
        sorted_values = self.sort_hand(self.card_list)
        for i in range(0, len(sorted_values)):
            for j in range(i + 1, len(sorted_values)):
                if (sorted_values[j-1].get_value()) + 1 == sorted_values[j].getvalue():
                    return True

        return False


    def is_three_of_a_kind(self):
        return False

    def is_two_pairs(self):
        if not self.is_one_pair():
            return 0

        pair_list = []

        for i in range(0, len(self.card_list)):
            for j in range(i + 1, len(self.card_list)):
                if self.card_list[i].get_value() == self.card_list[j].get_value():
                    pair_list.append(self.card_list[i].get_value())
                    pair_list.append(self.card_list[j].get_value())

        if len(pair_list) >= 4:
            pair_list.sort(reverse=True)
            sum = 0
            for i in range(4):
                sum += pair_list[i]
            return sum
        return 0

    def is_one_pair(self):

        for i in range(0, len(self.card_list)):
            for j in range(i + 1, len(self.card_list)):
                if self.card_list[i].get_value() == self.card_list[j].get_value():
                    return self.card_list[i].get_value() + self.card_list[j].get_value()
        return 0

    def is_high_card(self):
        return True

    def sort_hand(self, card_list):
        card_list_clone = card_list.copy()
        iteration = 0
        while iteration < len(card_list_clone):
            for i in range(len(card_list_clone)-1):
                if card_list_clone[i].get_value() < card_list_clone[i+1].get_value():
                    temp = card_list_clone[i]
                    card_list_clone[i] = card_list_clone [i+1]
                    card_list_clone[i+1] = temp
                iteration += 1
        return card_list_clone


if __name__ == '__main__':
    deckList = [
        Card("S", "A", True),
        Card("D", "A", True),
        Card("H", "4", True),
        Card("S", "Q", True),
        Card("H", "Q", True),
        Card("S", "4", True)
    ]
    deck = Deck(deckList)
    deck.get_ranking()
    print deck.is_one_pair()
    print deck.is_two_pairs()
