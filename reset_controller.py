##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# December 1, 2017
##############################

import cherrypy
import re, json
from _league_database import _league_database

class ResetController(object):
    def __init__(self, ldb, players_path, match_history_path, champions_path):
        self.ldb                    = ldb
        self.players_path           = players_path
        self.match_history_path     = match_history_path
        self.champions_path         = champions_path

    # Recreates database from .dat files.
    def PUT(self):
        output = {'result' : 'success'}

        # Reset ldb.
        try:
            self.ldb.delete_all_dictionaries()
            self.ldb.load_players(self.players_path)
            self.ldb.load_champions(self.champions_path)
            self.ldb.load_match_history(self.match_history_path)
            self.ldb.init_meta()
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)

        return json.dumps(output)

    # Resets one challenger player from .dat files.
    def PUT_PLAYER_KEY(self, key):
        # key = acc_id
        output = {'result' : 'success'}
        key = int(key)

        # Recreate an original ldb.
        orig_ldb = _league_database()
        orig_ldb.load_players(self.players_path)

        try:
            print(orig_ldb.get_player(key))
            self.ldb.players[key] = orig_ldb.get_player(key)
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)

        return json.dumps(output)

    # Resets one challenger player's match history from .dat files.
    def PUT_MATCH_KEY(self, key):
        # key = acc_id
        output = {'result' : 'success'}
        key = int(key)

        # Recreate an original ldb.
        orig_ldb = _league_database()
        orig_ldb.load_match_history(self.match_history_path)

        try:
            self.ldb.matches[key] = orig_ldb.get_match_history(key)
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)

        return json.dumps(output)

    # Resets one champion from .dat files.
    def PUT_CHAMPION_KEY(self, key):
        # key = champion_id
        output = {'result' : 'success'}
        key = int(key)

        # Recreate an original ldb.
        orig_ldb = _league_database()
        orig_ldb.load_champions(self.champions_path)

        try:
            self.ldb.champions[key] = orig_ldb.get_champion(key)
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)

        return json.dumps(output)

