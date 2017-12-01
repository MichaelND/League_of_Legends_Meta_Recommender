##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# December 1, 2017
##############################

import cherrypy
import re, json
from _league_database import _league_database

class ChampionController(object):
    def __init__(self, ldb):
        self.ldb  = ldb

    def GET(self):
        output = {}
        champions = []

        for champ_id in self.ldb.champions.keys():
            v = self.ldb.get_champion(champ_id)
            champions.append({'c_name': v['c_name'], 'image': v['image']})

        output['Champions'] = champions
        output['result']   = 'success'  

        return json.dumps(output)

    def GET_KEY(self, key):
        output = {}

        champ = self.ldb.get_champion(key)
        if champ is None:
            output['result']    = 'error'
            output['message']   = 'champion not found'
        else:
            output['c_name']    = champ['c_name']
            output['image']     = champ['image']
            output['champ_id']  = key
            output['result']    = 'success'

        return json.dumps(output)

    def POST(self):
        req = cherrypy.request.body.read().decode()
        req = json.loads(req)
        output = {}

        try:
            output['result']    = 'success'
            self.ldb.set_champion(req['champ_id'], req)
        except KeyError:
            output['result']    = 'error'
            output['message']   = 'invalid request'

        return json.dumps(output)

    def PUT_KEY(self, key):
        req = cherrypy.request.body.read().decode()
        req = json.loads(req)
        output = {}

        #TODO: Implementation on API side
        output['result'] = 'success'

        return json.dumps(output)