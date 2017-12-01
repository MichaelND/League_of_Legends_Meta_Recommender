##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# December 1, 2017
##############################


from _league_database import _league_database
import unittest
import requests
import json

PORT_NUM 				= '51049'
SITE_URL 				= 'http://student04.cse.nd.edu:' + PORT_NUM
PLAYERS_URL 			= SITE_URL + '/players/'
CHAMPION_URL 			= SITE_URL + '/champions/'
MATCH_HISTORY_URL 		= SITE_URL + '/matches/'
META_URL 				= SITE_URL + '/meta/'
RESET_URL 				= SITE_URL + '/reset/'
RESET_PLAYER_URL 		= RESET_URL + '/player/'
RESET_MATCH_HISTORY_URL = RESET_URL + '/match_history/'
RESET_CHAMPION_URL 		= RESET_URL + '/champion/'


class TestWebservice(unittest.TestCase):
    def reset_data(self):
        m = {}
        r = requests.put(RESET_URL, data = json.dumps(m))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_players_get(self):
        #get without account id
        # self.reset_data()
        r = requests.get(PLAYERS_URL)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        #get with account id
        account_id = 234873632
        self.reset_data()
        r = requests.get(PLAYERS_URL + str(account_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['wins'], 317)
        self.assertEqual(resp['losses'], 243)
        self.assertEqual(resp['acc_id'], '234873632')
        self.assertEqual(resp['name'], 'CHIEF KEITH')
        self.assertEqual(resp['lp'], 653)

    def test_players_put(self):
        # self.reset_data()
        account_id = 234873632
        
        player = {}
        player['wins']      = 317
        player['losses']    = 243
        player['name']      = 'CHIEF KEITH'
        player['lp']        = 653
        player['acc_id']    = '234873632'

        r = requests.put(PLAYERS_URL, data = json.dumps(player))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
    

    # def test_movies_put(self):
    #     self.reset_data()
    #     movie_id = 95

    #     r = requests.get(self.MOVIES_URL + str(movie_id))
    #     self.assertTrue(self.is_json(r.content.decode('utf-8')))
    #     resp = json.loads(r.content.decode('utf-8'))
    #     self.assertEqual(resp['title'], 'Broken Arrow (1996)')
    #     self.assertEqual(resp['genres'], 'Action|Thriller')

    #     m = {}
    #     m['title'] = 'ABC'
    #     m['genres'] = 'Sci-Fi|Fantasy'
    #     r = requests.put(self.MOVIES_URL + str(movie_id), data = json.dumps(m))
    #     self.assertTrue(self.is_json(r.content.decode('utf-8')))
    #     resp = json.loads(r.content.decode('utf-8'))
    #     self.assertEqual(resp['result'], 'success')

    #     r = requests.get(self.MOVIES_URL + str(movie_id))
    #     self.assertTrue(self.is_json(r.content.decode('utf-8')))
    #     resp = json.loads(r.content.decode('utf-8'))
    #     self.assertEqual(resp['title'], m['title'])
    #     self.assertEqual(resp['genres'], m['genres'])

    # def test_movies_delete(self):
    #     self.reset_data()
    #     movie_id = 95

    #     m = {}
    #     r = requests.delete(self.MOVIES_URL + str(movie_id), data = json.dumps(m))
    #     self.assertTrue(self.is_json(r.content.decode('utf-8')))
    #     resp = json.loads(r.content.decode('utf-8'))
    #     self.assertEqual(resp['result'], 'success')

    #     r = requests.get(self.MOVIES_URL + str(movie_id))
    #     self.assertTrue(self.is_json(r.content.decode('utf-8')))
    #     resp = json.loads(r.content.decode('utf-8'))
    #     self.assertEqual(resp['result'], 'error')
    #     #self.assertEqual(resp['message'], 'movie not found')

    # /players/

    # /champion/

    # /matches/

    # /meta/

    # /reset/


if __name__ == '__main__':
	print('Testing Port number: ', PORT_NUM)
	unittest.main()