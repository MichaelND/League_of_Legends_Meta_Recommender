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
			self.ldb.load_players('data/challenger.csv')
			self.ldb.load_champions('data/champions.csv')
			self.ldb.load_match_history('data/match_history.csv')

	def test_get_player(self):
			self.reset_data()
			player = self.ldb.get_player(ACC_ID)
			self.assertEqual(player['wins'], 317)
			self.assertEqual(player['losses'], 243)
			self.assertEqual(player['name'], 'CHIEF KEITH')
			self.assertEqual(player['lp'], 653)

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
			self.assertEqual(match_history[0]['lane'], 'BOTTOM')
			self.assertEqual(match_history[0]['game_id'], 2656410494)
			self.assertEqual(match_history[0]['champion_id'], 429)
			self.assertEqual(match_history[0]['queue'], 420)
			self.assertEqual(match_history[0]['role'], 'DUO_CARRY')
			self.assertEqual(match_history[0]['timestamp'], 1511683429568)

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


if __name__ == "__main__":
	unittest.main()

