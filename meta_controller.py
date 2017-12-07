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
        output = {'result' : 'success'}

        try:
            output.update(self.ldb.get_all_meta())
        except Exception as e:
            print('Error: ' + str(e))
            output['result'] = 'error'
        return json.dumps(output)

    def GET_KEY(self, key):
        #This function will make a request to our webservice to get the meta for a specific lane. 
        output = {'result' : 'success'}
        key = int(key)

        try:
            output.update(self.ldb.get_n_meta(key))
            print(output)
        except Exception as e:
            print('Error: ' + str(e))
            output['result'] = 'error'
        return json.dumps(output)

    def POST_KEY(self, key):
        #This function will make a request to our webservice to get the meta for a specific lane. 
        output = {'result' : 'success'}
        key = int(key)
        
        return json.dumps(output)