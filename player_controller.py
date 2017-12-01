##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# December 1, 2017
##############################

import cherrypy
import re, json

class PlayerController(object):
    def __init__(self, ldb):
        self.ldb = ldb

    def GET(self):
        output = {'result' : 'success'}
        try:
            playerList = []
            for p in self.ldb.players.keys():
                v = self.ldb.get_player(p)
                playerList.append({'acc_id' : p, 'wins' : v['wins'], 'losses' : v['losses'], 'name' : v['name'], 'lp' : v['lp']})
            output['players'] = playerList
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)

        return json.dumps(output)

    def POST(self):
        output = {'result' : 'success'}
        try:
            dictData = cherrypy.request.body.read().decode()
            dictData = json.loads(dictData)
            self.ldb.set_player(dictData['acc_id'], dictData)
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)

        return json.dumps(output)
    
    def GET_KEY(self, key):
        # key = acc_id
        output = {'result' : 'success'}
        player = self.ldb.get_player(key)
        if player is None:
            output['result'] = 'error'
            output['message'] = 'player does not exist'
        else:
            output['acc_id'] = key
            output['wins'] = player['wins']
            output['losses'] = player['losses']
            output['name'] = player['name']
            output['lp'] = player['lp']
        return json.dumps(output)

    def DELETE_KEY(self, key):
        # key = acc_id
        output = {'result' : 'success'}
        try:
            self.ldb.delete_player(key)
        except Exception as e:
            output['result'] = 'error'
            output['message'] = str(e)
        return json.dumps(output)

