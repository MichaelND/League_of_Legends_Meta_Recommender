##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# December 1, 2017
##############################

import cherrypy
import re, json
from _league_database import _league_database

class MetaController(object):

    def __init__(self, ldb):
        self.ldb  = ldb

    def GET(self):
        output = {}

        #TODO: Implementation on API side
        output['result'] = 'success'

        return json.dumps(output)

    def GET_KEY(self, key):
        output = {}

        key = int(key)

        #TODO: Implementation on API side
        output['result'] = 'success'
        
        return json.dumps(output)