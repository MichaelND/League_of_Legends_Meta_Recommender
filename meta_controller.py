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
        #This function will make a request to our webservice to get the meta for each lane.
        output = {}

        #TODO: Implementation on API side
        output['result'] = 'success'

        return json.dumps(output)

    def GET_KEY(self, key):
        #This function will make a request to our webservice to get the meta for a specific lane. 
        output = {}

        key = int(key)

        #TODO: Implementation on API side
        output['result'] = 'success'
        
        return json.dumps(output)