##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# December 1, 2017
##############################

import cherrypy
import re, json

class MatchesController(object):
    def __init__(self, ldb):
        self.ldb = ldb

    # GET all matches of all players
    def GET(self):
        output = {'result' : 'success'}
        try:
            for k, v in self.ldb.matches.items():
                # k = acc_id
                # v = list of their games
                gameList = []
                for i in range(0, len(v)):
                    gameList.append(v[i])
                output[k] = gameList
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)

    # GET matches of player by acc_id
    def GET_KEY(self, key):
        # key = acc_id
        output = {'result' : 'success'}
        match_history = self.ldb.get_match_history(key)
        if match_history is None:
            output['result'] = 'error'
            output['message'] = 'account does not exist'
        else:
            output['matches'] = match_history
        return json.dumps(output)

    # POST mataches of player
    def POST_KEY(self, key):
        # key = acc_id
        output = {'result' : 'success'}
        try:
            dictData = cherrypy.request.body.read().decode()
            dictData = json.loads(dictData)
            self.ldb.set_match_history(key, dictData, dictData['match_num'])
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)

    # DELETE a player's matches by acc_id
    def DELETE_KEY(self, key):
        # key = acc_id
        output = {'result' : 'success'}
        try:
            self.ldb.delete_match_history(key)
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)

