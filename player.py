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

            print card_list_raw

            card_list = []
            for card in card_list_raw:
                card_list.append(Card(card["suit"], card["rank"], True))
            deck = Deck(card_list)
            ranking = deck.get_ranking()
            max_rank = 60 * 30939.0

            return max(int(ranking / max_rank * stack), game_state["minimum_raise"])

        except:
            traceback.print_exc()
            return 0


    def showdown(self, game_state):
        pass
