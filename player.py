import traceback
from deck import Deck
from card import Card
import math


class Player:
    VERSION = "0.1.1"

    def betRequest(self, game_state):
        try:
            card_list_raw = []
            stack = 0
            for person in game_state["players"]:
                if person["id"] == 4:
                    card_list_raw = person["hole_cards"]
                    stack = person["stack"]

            card_list_raw.extend(game_state["community_cards"])



            card_list = []
            for card in card_list_raw:
                card_list.append(Card(card["suit"], card["rank"], True))
            deck = Deck(card_list)

            if len(card_list) == 2:
                if deck.is_one_pair():
                    return game_state["current_buy_in"] + game_state["minimum_raise"]
                if (abs(card_list[0].get_value() - card_list[1].get_value()) < 5) or (card_list[0].get_value() > 10 or card_list[1].get_value() > 10):
                    return game_state["current_buy_in"]

            ranking = deck.get_ranking()
            max_rank = 60 * 30.0
            print card_list
            print ranking / max_rank
            return max(int(ranking / max_rank * stack), game_state["minimum_raise"])

        except:
            traceback.print_exc()
            return 0


    def showdown(self, game_state):
        pass
