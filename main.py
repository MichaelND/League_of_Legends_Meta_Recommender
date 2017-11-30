##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# December 1, 2017
##############################

import cherrypy
from _league_database import _league_database
from matches_controller import MatchesController
from player_controller import PlayerController
from meta_controller import MetaController
from champion_controller import ChampionController

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    ldb = _league_database()
    matches_controller = MatchesController(ldb)
    player_controller = PlayerController(ldb)
    meta_controller = MetaController(ldb)
    champion_controller = ChampionController(ldb)

    #player
    dispatcher.connect('player_get', '/players/', controller = player_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('player_post', '/players/', controller = player_controller, action = 'POST', conditions = dict(method=['POST']))
    #player:acc_id
    dispatcher.connect('player_get_acc_id', '/players/:acc_id', controller = player_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('player_delete_acc_id', '/players/:acc_id', controller = player_controller, action = 'DELETE', conditions = dict(method=['DELETE']))

    #matches
    dispatcher.connect('matches_get', '/matches/', controller = matches_controller, action = 'GET', conditions = dict(method=['GET']))
    #matches/:acc_id
    dispatcher.connect('matches_get_acc_id', '/matches/:acc_id', controller = matches_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('matches_post_acc_id', '/matches/:acc_id', controller = matches_controller, action = 'POST', conditions = dict(method=['POST']))
    dispatcher.connect('matches_delete_acc_id', '/matches/:acc_id', controller = matches_controller, action = 'DELETE', conditions = dict(method=['DELETE']))

    #champion
    dispatcher.connect('champion_get', '/champion/', controller = champion_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('champion_post', '/champion/', controller = champion_controller, action = 'POST', conditions = dict(method=['POST']))
    #champion/:champ_id
    dispatcher.connect('champion_get_champ_id', '/champion/:champ_id', controller = champion_controller, action = 'GET', conditions = dict(method=['GET']))
    #champion/:meta_vote
    dispatcher.connect('champion_put_meta_vote', '/champion/:meta_vote', controller = champion_controller, action = 'PUT', conditions = dict(method=['PUT']))

    #meta
    dispatcher.connect('meta_get', '/meta/', controller = meta_controller, action = 'GET', conditions = dict(method=['GET']))
    #meta/:lane
    dispatcher.connect('meta_get_lane', '/meta/:lane', controller = meta_controller, action = 'GET', conditions = dict(method=['GET']))
    

    #set up server
    conf = {'global':
                {'server.socket_host': 'student04.cse.nd.edu',
                'server.socket_port': 51080},
            '/': {'request.dispatch': dispatcher} }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

if __name__ == '__main__':
    start_service()
