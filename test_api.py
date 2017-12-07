##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# November 27, 2017
##############################

from _league_database import _league_database
import unittest

ACC_ID 		= 234873632
CHAMP_ID 	= 432

# Anthony's NOTE:
# TODO:
#     gets that return NONE

class TestLeageDatabase(unittest.TestCase):
	ldb = _league_database()

	def reset_data(self):
			#reset all data to begin with
			self.ldb.delete_all_dictionaries()
			self.ldb.load_players('data/challenger_1m.csv')
			self.ldb.load_champions('data/champions_1m.csv')
			self.ldb.load_match_history('data/match_history_1m.csv')
			self.ldb.init_meta()

	def test_get_player(self):
			self.reset_data()
			player = self.ldb.get_player(ACC_ID)
			self.assertEqual(player['wins'], 319)
			self.assertEqual(player['losses'], 245)
			self.assertEqual(player['name'], 'CHIEF KEITH')
			self.assertEqual(player['lp'], 649)

	def test_get_player_null(self):
			self.reset_data()
			player = self.ldb.get_player(1337)
			self.assertEqual(player, None)

	def test_set_player(self):
			self.reset_data()
			player = self.ldb.get_player(ACC_ID)
			player['name'] = 'ABC'
			self.ldb.set_player(ACC_ID, player)
			player = self.ldb.get_player(ACC_ID)
			self.assertEqual(player['name'], 'ABC')

	def test_delete_player(self):
			self.reset_data()
			self.ldb.delete_player(ACC_ID)
			player = self.ldb.get_player(ACC_ID)
			self.assertEqual(player, None)

	def test_get_champion(self):
			self.reset_data()
			champion = self.ldb.get_champion(CHAMP_ID)
			self.assertEqual(champion['c_name'], 'Bard') #champion name
			self.assertEqual(champion['image'], 'Bard.png') #image

	def test_set_champion(self):
			self.reset_data()
			champion = self.ldb.get_champion(CHAMP_ID)
			champion['c_name'] = 'branddd'
			champion['image'] = 'brddd.png'
			self.ldb.set_champion(CHAMP_ID, champion)
			champion = self.ldb.get_champion(CHAMP_ID)
			self.assertEqual(champion['c_name'], 'branddd')
			self.assertEqual(champion['image'], 'brddd.png')

	def test_delete_champion(self):
			self.reset_data()
			self.ldb.delete_champion(CHAMP_ID)
			champion = self.ldb.get_champion(CHAMP_ID)
			self.assertEqual(champion, None)

	def test_get_match_history(self):
			self.reset_data()
			match_history = self.ldb.get_match_history(ACC_ID)
			self.assertEqual(match_history[0]['lane'], 'MID')
			self.assertEqual(match_history[0]['game_id'], 2661531048)
			self.assertEqual(match_history[0]['champion_id'], 101)
			self.assertEqual(match_history[0]['queue'], 420)
			self.assertEqual(match_history[0]['role'], 'SOLO')
			self.assertEqual(match_history[0]['timestamp'], 1512267077431)

	def test_set_match_history(self):
			self.reset_data()
			match = self.ldb.get_match_history(ACC_ID)[0]
			match['lane'] = 'odyssey'
			match['game_id'] = 1337
			match['champion_id'] = 22
			match['queue'] = 717
			match['role'] = 'switch'
			match['timestamp'] = 1941782
			self.ldb.set_match_history(ACC_ID, match, 0)
			match = self.ldb.get_match_history(ACC_ID)
			self.assertEqual(match[0]['lane'], 'odyssey')
			self.assertEqual(match[0]['game_id'], 1337)
			self.assertEqual(match[0]['champion_id'], 22)
			self.assertEqual(match[0]['queue'], 717)
			self.assertEqual(match[0]['role'], 'switch')
			self.assertEqual(match[0]['timestamp'], 1941782)

	def test_delete_match_history(self):
			self.reset_data()
			self.ldb.delete_match_history(ACC_ID)
			match = self.ldb.get_match_history(ACC_ID)
			self.assertEqual(match, None)

	#- Advanced Function Tests ------------------------#
	def test_get_all_meta(self):
			self.reset_data()
			all_meta_dict = self.ldb.get_all_meta()
			self.assertEqual(all_meta_dict['TOP']['Jayce'], 220)
			self.assertEqual(all_meta_dict['JUNGLE']['Khazix'], 200)
			self.assertEqual(all_meta_dict['MID']['Azir'], 254)
			self.assertEqual(all_meta_dict['BOTTOM']['Ashe'], 81)

	def test_get_n_meta(self):
			self.reset_data()
			n_meta_dict = self.ldb.get_n_meta(-1)
			self.assertEqual(len(n_meta_dict), 0)

			n_meta_dict = self.ldb.get_n_meta(2)
			for k, v in n_meta_dict.items():
				self.assertEqual(len(v), 2)
			self.assertEqual(n_meta_dict['TOP'][0][0], 'Pantheon')
			self.assertEqual(n_meta_dict['TOP'][0][1], 243)
			self.assertEqual(n_meta_dict['TOP'][1][0], 'Jayce')
			self.assertEqual(n_meta_dict['TOP'][1][1], 220)
			self.assertEqual(n_meta_dict['JUNGLE'][0][0], 'JarvanIV')
			self.assertEqual(n_meta_dict['JUNGLE'][0][1], 358)
			self.assertEqual(n_meta_dict['JUNGLE'][1][0], 'RekSai')
			self.assertEqual(n_meta_dict['JUNGLE'][1][1], 264)
			self.assertEqual(n_meta_dict['MID'][0][0], 'Ryze')
			self.assertEqual(n_meta_dict['MID'][0][1], 296)
			self.assertEqual(n_meta_dict['MID'][1][0], 'Azir')
			self.assertEqual(n_meta_dict['MID'][1][1], 254)
			self.assertEqual(n_meta_dict['BOTTOM'][0][0], 'Tristana')
			self.assertEqual(n_meta_dict['BOTTOM'][0][1], 370)
			self.assertEqual(n_meta_dict['BOTTOM'][1][0], 'Kalista')
			self.assertEqual(n_meta_dict['BOTTOM'][1][1], 219)

	def test_update_meta_vote(self):
		pass

if __name__ == "__main__":
	unittest.main()

