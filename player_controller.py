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
		return json.dumps(output)

	def POST(self):
		output = {'result' : 'success'}
		return json.dumps(output)
	
	def GET_KEY(self, key):
		output = {'result' : 'success'}
		return json.dumps(output)

	def DELETE_KEY(self, key):
		output = {'result' : 'success'}
		return json.dumps(output)
