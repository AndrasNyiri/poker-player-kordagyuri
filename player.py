class Player:
    VERSION = "0.1.1"

    def betRequest(self, game_state):
        print game_state
        return 0

    def showdown(self, game_state):
        pass


if __name__ == "__main__":
    game_state = "{u'orbits': 13, u'community_cards': [], u'round': 78, u'current_buy_in': 1040, u'game_id': u'5af955da2bc5600004000061', u'pot': 1120, u'minimum_raise': 960, u'dealer': 4, u'bet_index': 9, u'small_blind': 40, u'in_action': 4, u'tournament_id': u'5af57bd9204a990004000002', u'big_blind': 80, u'players': [{u'version': u'Default Python folding player', u'name': u'Game On', u'id': 0, u'status': u'out', u'stack': 0, u'bet': 0, u'time_used': 16136}, {u'version': u'0.1', u'name': u'pokerbot69', u'id': 1, u'status': u'active', u'stack': 3856, u'bet': 1040, u'time_used': 660708}, {u'version': u'Default Python folding player', u'name': u'pYker', u'id': 2, u'status': u'out', u'stack': 0, u'bet': 0, u'time_used': 205257}, {u'version': u'0.0.1', u'name': u'TorMentors', u'id': 3, u'status': u'out', u'stack': 0, u'bet': 0, u'time_used': 7507}, {u'version': u'Default Python folding player', u'name': u'KordaGyuri', u'hole_cards': [{u'rank': u'Q', u'suit': u'diamonds'}, {u'rank': u'8', u'suit': u'hearts'}], u'id': 4, u'status': u'active', u'stack': 24, u'bet': 80, u'time_used': 694960}, {u'version': u'Default Java folding player', u'name': u'The known ferrets', u'id': 5, u'status': u'out', u'stack': 0, u'bet': 0, u'time_used': 12862}]}"
    Player().betRequest(game_state)
