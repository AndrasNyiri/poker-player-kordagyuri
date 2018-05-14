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
        if self.sort_hand(self.card_list)[0].get_value() == 10 and self.is_staight_flush() != 0:
            return self.is_staight_flush()
        return 0



    def is_staight_flush(self):
        if self.is_straight() != 0 and self.is_flush() != 0:
            return self.is_flush()
        return 0

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
            value = 0
            count = 0
            for j in range(i + 1, len(sorted_values)):
                if (sorted_values[j-1].get_value()) + 1 == sorted_values[j].get_value():
                    count += 1
                    value += sorted_values[j - 1].get_value()
                    if count == 4:
                        return value

        for i in range(len(sorted_values)):
            if sorted_values[i].get_value() == 14:
                sorted_values[i].value = 1

        sorted_values = self.sort_hand(sorted_values)

        for i in range(0, len(sorted_values)):
            value = 0
            count = 0
            for j in range(i + 1, len(sorted_values)):
                if (sorted_values[j-1].get_value()) + 1 == sorted_values[j].get_value():
                    count += 1
                    value += sorted_values[j - 1].get_value()
                    if count == 4:
                        return value

        return 0


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

    def sort_hand(self, list_):
        if list is None:
            card_list_clone = list(self.card_list)
        else:
            card_list_clone = list(list_)

        iteration = 0
        while iteration < len(card_list_clone):
            for i in range(len(card_list_clone) - 1):
                if card_list_clone[i].get_value() > card_list_clone[i+1].get_value():
                    temp = card_list_clone[i]
                    card_list_clone[i] = card_list_clone[i+1]
                    card_list_clone[i+1] = temp
            iteration += 1
        return card_list_clone





if __name__ == '__main__':
    Deck()

