##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# November 27, 2017
##############################

from _league_database import _league_database
import unittest

ACC_ID 		= 234873632
CHAMP_ID 	= 432

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
			self.assertEquals(player['wins'], 317)
			self.assertEquals(player['losses'], 243)
			self.assertEquals(player['name'], 'CHIEF KEITH')
			self.assertEquals(player['lp'], 653)

	def test_get_player_null(self):
			self.reset_data()
			player = self.ldb.get_player(1337)
			self.assertEquals(player, None)

	def test_set_player(self):
			self.reset_data()
			player = self.ldb.get_player(ACC_ID)
			player['name'] = 'ABC'
			self.ldb.set_player(ACC_ID, player)
			player = self.ldb.get_player(ACC_ID)
			self.assertEquals(player['name'], 'ABC')

	def test_delete_player(self):
			self.reset_data()
			self.ldb.delete_player(ACC_ID)
			player = self.ldb.get_player(ACC_ID)
			self.assertEquals(player, None)

	def test_get_champion(self):
			self.reset_data()
			champion = self.ldb.get_champion(CHAMP_ID)
			self.assertEquals(champion['c_name'], 'Bard') #champion name
			self.assertEquals(champion['image'], 'Bard.png') #image

	def test_set_champion(self):
			self.reset_data()
			champion = self.ldb.get_champion(CHAMP_ID)
			champion['c_name'] = 'branddd'
			champion['image'] = 'brddd.png'
			self.ldb.set_champion(CHAMP_ID, champion)
			champion = self.ldb.get_champion(CHAMP_ID)
			self.assertEquals(champion['c_name'], 'branddd')
			self.assertEquals(champion['image'], 'brddd.png')

	def test_delete_champion(self):
			self.reset_data()
			self.ldb.delete_champion(CHAMP_ID)
			champion = self.ldb.get_champion(CHAMP_ID)
			self.assertEquals(champion, None)

	def test_get_match_history(self):
			self.reset_data()
			match_history = self.ldb.get_match_history(ACC_ID)
			# self.assertEquals(match_history, 3.945731303772336)
			# match_history = self.ldb.get_match_history(110)
			# self.assertEquals(match_history, 4.234957020057307)
			# match_history = self.ldb.get_match_history(1)
			# self.assertEquals(match_history, 4.146846413095811)

	# def test_get_highest_rated_movie_1(self):
	#         self.reset_data()
	#         hrm_mid = self.ldb.get_highest_rated_movie()
	#         hrm_rating = self.ldb.get_rating(hrm_mid)
	#         hrm = self.ldb.get_movie(hrm_mid)
	#         hrm_name = hrm[0]
	#         self.assertEquals(hrm_mid, 787)
	#         self.assertEquals(hrm_name, 'Gate of Heavenly Peace, The (1995)')
	#         self.assertEquals(hrm_rating, 5.0)

	# def test_set_user_movie_rating_1(self):
	#         self.reset_data()
	#         self.ldb.set_user_movie_rating(41, 787, 2)
	#         rating = self.ldb.get_rating(787)
	#         self.assertEquals(rating, 4.25)

	# def test_set_user_movie_rating_2(self):
	#         self.reset_data()
	#         self.ldb.set_user_movie_rating(41, 787, 2)
	#         self.ldb.set_user_movie_rating(101, 787, 4)
	#         rating = self.ldb.get_rating(787)
	#         self.assertEquals(rating, 4.2)

	# def test_set_and_get_movie_ratings(self):
	#         self.reset_data()
	#         self.ldb.set_user_movie_rating(41, 787, 2)
	#         self.ldb.set_user_movie_rating(101, 787, 4)
	#         hrm_mid = self.ldb.get_highest_rated_movie()
	#         hrm_rating = self.ldb.get_rating(hrm_mid)
	#         hrm = self.ldb.get_movie(hrm_mid)
	#         hrm_name = hrm[0]
	#         self.assertEquals(hrm_mid, 989)
	#         self.assertEquals(hrm_name, 'Schlafes Bruder (Brother of Sleep) (1995)')
	#         self.assertEquals(hrm_rating, 5.0)

	# def test_get_user_movie_rating(self):
	#         self.reset_data()
	#         rating = self.ldb.get_user_movie_rating(6030, 32)
	#         self.assertEquals(rating, 5)

if __name__ == "__main__":
	unittest.main()

