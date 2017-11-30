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

        for mid in self.ldb.champ_id #this will get all champions but our ooapi needs to be update for this method
            champion = {}
            champion['c_name']  = self.ldb.champ_id[champ_id]['c_name']
            champion['image']   = self.ldb.champ_id[champ_id]['image']

            output['champion'].append(champion)

        output['result'] = 'success'

        return json.dumps(output)

    def GET_KEY(self, key):
        output = {}
        output['result'] = 'success'

        return json.dumps(output)

    def POST(self):
        req = cherrypy.request.body.read().decode()
        req = json.loads(req)
        output = {}

        output['result'] = 'success'

        return json.dumps(output)

    def PUT_KEY(self, key):
        req = cherrypy.request.body.read().decode()
        req = json.loads(req)
        output = {}

        output['result'] = 'success'

        return json.dumps(output)