#*******************************
# Anthony Luc, Michael Wang
# ParadigmsFinal
# December 1, 2017
#*******************************


#*******************************************************
# Imports
#*******************************************************
import cherrypy
from _league_database import _league_database
from matches_controller import MatchesController
from player_controller import PlayerController
from meta_controller import MetaController
from champion_controller import ChampionController
from reset_controller import ResetController
from option_controller import OptionController

#*******************************************************
# Global Variables
#*******************************************************
PORT                        = 51049
PLAYER_DATA_PATH            = 'data/challenger_1m.csv'
CHAMPION_DATA_PATH          = 'data/champions_1m.csv'
MATCH_HISTORY_DATA_PATH     = 'data/match_history_1m.csv'

#*******************************************************
# init_db
#*******************************************************
def init_db(ldb):
    ldb.load_players(PLAYER_DATA_PATH)
    ldb.load_champions(CHAMPION_DATA_PATH)
    ldb.load_match_history(MATCH_HISTORY_DATA_PATH)
    ldb.init_meta()

#*******************************************************
# CORS
#*******************************************************

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"

#*******************************************************
# start_service
#*******************************************************
def start_service():
    ### Declare variables.
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    ldb = _league_database()

    ### Initialize variables.
    init_db(ldb)

    ### Declare controllers.
    matches_controller = MatchesController(ldb)
    player_controller = PlayerController(ldb)
    meta_controller = MetaController(ldb)
    champion_controller = ChampionController(ldb)
    reset_controller = ResetController(ldb, PLAYER_DATA_PATH, MATCH_HISTORY_DATA_PATH, CHAMPION_DATA_PATH)
    option_controller = OptionController()

    #/player/
    dispatcher.connect('player_get', '/players/', controller = player_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('player_post', '/players/', controller = player_controller, action = 'POST', conditions = dict(method=['POST']))
    #/player/:key
    dispatcher.connect('player_get_key', '/players/:key', controller = player_controller, action = 'GET_KEY', conditions = dict(method=['GET']))
    dispatcher.connect('player_delete_key', '/players/:key', controller = player_controller, action = 'DELETE_KEY', conditions = dict(method=['DELETE']))

    #/matches/
    dispatcher.connect('matches_get', '/matches/', controller = matches_controller, action = 'GET', conditions = dict(method=['GET']))
    #/matches/:key
    dispatcher.connect('matches_get_key', '/matches/:key', controller = matches_controller, action = 'GET_KEY', conditions = dict(method=['GET']))
    dispatcher.connect('matches_post_key', '/matches/:key', controller = matches_controller, action = 'POST_KEY', conditions = dict(method=['POST']))
    dispatcher.connect('matches_delete_key', '/matches/:key', controller = matches_controller, action = 'DELETE_KEY', conditions = dict(method=['DELETE']))

    #/champion/
    dispatcher.connect('champion_get', '/champion/', controller = champion_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('champion_post', '/champion/', controller = champion_controller, action = 'POST', conditions = dict(method=['POST']))
    #/champion/:key
    dispatcher.connect('champion_get_key', '/champion/:key', controller = champion_controller, action = 'GET_KEY', conditions = dict(method=['GET']))
    dispatcher.connect('champion_delete_key', '/champion/:key', controller = champion_controller, action = 'DELETE_KEY', conditions = dict(method=['DELETE']))

    #/meta/
    dispatcher.connect('meta_get', '/meta/', controller = meta_controller, action = 'GET', conditions = dict(method=['GET']))
    #/meta/:key
    dispatcher.connect('meta_get_key', '/meta/:key', controller = meta_controller, action = 'GET_KEY', conditions = dict(method=['GET']))
    dispatcher.connect('meta_post_key', '/meta/:key', controller = meta_controller, action = 'POST_KEY', conditions = dict(method=['POST']))

    #/reset/
    dispatcher.connect('reset_put', '/reset/', controller = reset_controller, action = 'PUT', conditions = dict(method=['PUT']))
    #/reset/:key
    dispatcher.connect('reset_put_player_key', '/reset/players/:key', controller = reset_controller, action = 'PUT_PLAYER_KEY', conditions = dict(method=['PUT']))
    dispatcher.connect('reset_put_matches_key', '/reset/matches/:key', controller = reset_controller, action = 'PUT_MATCH_KEY', conditions = dict(method=['PUT']))
    dispatcher.connect('reset_put_champion_key', '/reset/champion/:key', controller = reset_controller, action = 'PUT_CHAMPION_KEY', conditions = dict(method=['PUT']))

    #Connect
    dispatcher.connect('player_get_option', '/players/', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('player_post_option', '/players/', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('player_get_key_option', '/players/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('player_delete_key_option', '/players/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    
    dispatcher.connect('matches_get_option', '/matches/', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('matches_get_key_option', '/matches/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('matches_post_key_option', '/matches/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('matches_delete_key_option', '/matches/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    
    dispatcher.connect('champion_get_option', '/champion/', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('champion_post_option', '/champion/', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('champion_get_key_option', '/champion/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('champion_delete_key_option', '/champion/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))

    dispatcher.connect('meta_get_option', '/meta/', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('meta_get_key_option', '/meta/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('meta_post_key_option', '/meta/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    
    dispatcher.connect('reset_put_option', '/reset/', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('reset_put_player_key_option', '/reset/players/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('reset_put_matches_key_option', '/reset/matches/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('reset_put_champion_key_option', '/reset/champion/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))

    #set up server
    conf = {'global':
                {'server.socket_host': 'student04.cse.nd.edu',
                'server.socket_port': PORT},
            '/': {'request.dispatch': dispatcher,
                'tools.CORS.on': True} }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)


#*******************************************************
# Main
#*******************************************************
if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
