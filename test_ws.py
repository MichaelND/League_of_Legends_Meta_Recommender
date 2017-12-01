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
CHAMPION_URL 			= SITE_URL + '/champion/'
MATCH_HISTORY_URL 		= SITE_URL + '/matches/'
META_URL 				= SITE_URL + '/meta/'
RESET_URL 				= SITE_URL + '/reset/'
RESET_PLAYER_URL 		= RESET_URL + '/players/'
RESET_MATCH_HISTORY_URL = RESET_URL + '/matches/'
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
        self.reset_data()
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

    def test_players_post(self):
        #post without account id
        self.reset_data()
        
        player = {}
        player['wins']      = 317
        player['losses']    = 243
        player['name']      = 'CHIEF KEITH'
        player['lp']        = 653
        player['acc_id']    = '234873632'

        r = requests.post(PLAYERS_URL, data = json.dumps(player))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
    
    def test_players_delete(self):
        #delete with account id
        self.reset_data()
        account_id = 234873632

        d = {}
        r = requests.delete(PLAYERS_URL + account_id, data = json.dumps(d))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

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