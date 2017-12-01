##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# December 1, 2017
##############################


from _league_database import _league_database
import unittest


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


class TestWebservice():
    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, data = json.dumps(m))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False


    # /players/

    # /champion/

    # /matches/

    # /meta/

    # /reset/


if __name__ == '__main__':
	print('Testing Port number: ', PORT_NUM)
	unittest.main()