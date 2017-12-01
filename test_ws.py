##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# December 1, 2017
##############################


from _league_database import _league_database
import unittest
import requests
import json

PORT_NUM 				= '51080'
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

    # /players/ unit tests

    # /champion/ unit tests
    def test_champion_get(self):
        #get without account id
        self.reset_data()
        r = requests.get(CHAMPION_URL)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

    def test_champion_get_key(self):
        self.reset_data()
        account_id = 266
        r = requests.get(CHAMPION_URL + str(account_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['c_name'], 'Aatrox')
        self.assertEqual(resp['image'], 'Aatrox.png')
        self.assertEqual(resp['champ_id'], '266')

    def test_champion_post_key(self):
        self.reset_data()
        champ_id = 266
        t = {}  # test dictionary
        t['c_name'] = 'Michael'
        t['image'] = 'Michael.png'
        t['champ_id'] = champ_id
        # TODO: META VOTE

        # Make POST request
        r = requests.post(CHAMPION_URL, data = json.dumps(t))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # GET updated value
        r = requests.get(CHAMPION_URL + str(champ_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['c_name'], 'Michael')
        self.assertEqual(resp['image'], 'Michael.png')
        self.assertEqual(resp['champ_id'], str(champ_id))

    def test_champion_delete(self):
        self.reset_data()
        champ_id = 266

        # Make DELETE request
        r = requests.delete(CHAMPION_URL + str(champ_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # Verify null
        r = requests.get(CHAMPION_URL + str(champ_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        self.assertEqual(resp['message'], 'champion not found')


    # /matches/

    # /meta/

    # /reset/


if __name__ == '__main__':
	print('Testing Port number: ', PORT_NUM)
	unittest.main()