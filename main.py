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

#*******************************************************
# Global Variables
#*******************************************************
PORT                        = 51080
PLAYER_DATA_PATH            = 'data/challenger.csv'
CHAMPION_DATA_PATH          = 'data/champions.csv'
MATCH_HISTORY_DATA_PATH     = 'data/match_history.csv'

#*******************************************************
# init_db
#*******************************************************
def init_db(ldb):
    ldb.load_players(PLAYER_DATA_PATH)
    ldb.load_champions(PLAYER_DATA_PATH)
    ldb.load_match_history(MATCH_HISTORY_DATA_PATH)

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
    dispatcher.connect('champion_put_key', '/champion/:key', controller = champion_controller, action = 'PUT_KEY', conditions = dict(method=['PUT']))

    #/meta/
    dispatcher.connect('meta_get', '/meta/', controller = meta_controller, action = 'GET', conditions = dict(method=['GET']))
    #/meta/:key
    dispatcher.connect('meta_get_lane', '/meta/:key', controller = meta_controller, action = 'GET_KEY', conditions = dict(method=['GET']))
    

    #set up server
    conf = {'global':
                {'server.socket_host': 'student04.cse.nd.edu',
                'server.socket_port': PORT},
            '/': {'request.dispatch': dispatcher} }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)


#*******************************************************
# Main
#*******************************************************
if __name__ == '__main__':
    start_service()
