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