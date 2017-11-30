# Michael Wang
# October 28, 2017
# CherryPy

import cherrypy
from _movie_database import _movie_database
from movies_cont import MovieController
from users_cont import UserController
from recommend_cont import RecommendationController
from ratings_cont import RatingController
from reset_cont import ResetController


def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    myd = _movie_database()
    movie_controller = MovieController(myd)
    user_controller = UserController(myd)
    recommendation_controller = RecommendationController(myd)
    rating_controller = RatingController(myd)
    reset_controller = ResetController(myd)

    #movies
    dispatcher.connect('movie_get', '/movies/', controller = movie_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('movie_post', '/movies/', controller = movie_controller, action = 'POST', conditions = dict(method=['POST']))
    dispatcher.connect('movie_delete', '/movies/', controller = movie_controller, action = 'DELETE', conditions = dict(method=['DELETE']))
    
    #movies:key
    dispatcher.connect('movie_get_key', '/movies/:key', controller = movie_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('movie_put_key', '/movies/:key', controller = movie_controller, action = 'PUT', conditions = dict(method=['PUT']))
    dispatcher.connect('movie_delete_key', '/movies/:key', controller = movie_controller, action = 'DELETE', conditions = dict(method=['DELETE']))

    #users
    dispatcher.connect('user_get', '/users/', controller = user_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('user_post', '/users/', controller = user_controller, action = 'POST', conditions = dict(method=['POST']))
    dispatcher.connect('user_delete', '/users/', controller = user_controller, action = 'DELETE', conditions = dict(method=['DELETE']))
    
    #users:key
    dispatcher.connect('user_get_key', '/users/:key', controller = user_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('user_put', '/users/:key', controller = user_controller, action = 'PUT', conditions = dict(method=['PUT']))
    dispatcher.connect('user_delete_key', '/users/:key', controller = user_controller, action = 'DELETE', conditions = dict(method=['DELETE']))

    #Recommendataions
    dispatcher.connect('recommendation_delete', '/recommendations/', controller = recommendation_controller, action = 'DELETE', conditions = dict(method=['DELETE']))
    dispatcher.connect('recommendation_get_key', '/recommendations/:key', controller = recommendation_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('recommendation_put_key', '/recommendations/:key', controller = recommendation_controller, action = 'PUT', conditions = dict(method=['PUT']))

    #Ratings
    dispatcher.connect('rating_get_key', '/ratings/:key', controller = rating_controller, action = 'GET', conditions = dict(method=['GET']))

    #Reset
    dispatcher.connect('reset_put', '/reset/', controller = reset_controller, action = 'PUT', conditions = dict(method=['PUT']))
    dispatcher.connect('reset_put_key', '/reset/:key', controller = reset_controller, action = 'PUT', conditions = dict(method=['PUT']))

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
