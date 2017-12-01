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

    def GET(self):
        output = {'result' : 'success'}
        try:
            for k, v in self.ldb.matches.items():
                # k = acc_id
                # v = all games
                gameList = []
                for i in range(0, len(v)):
                    gameList.append(v[i])
                output[k] = gameList
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)

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

    def DELETE_KEY(self, key):
        # key = acc_id
        output = {'result' : 'success'}
        try:
            self.ldb.delete_match_history(key)
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)

