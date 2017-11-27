##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# November 27, 2017
##############################

from _league_database import _league_database
import unittest

class TestLeageDatabase(unittest.TestCase):
        ldb = _league_database()

    def reset_data(self):
            #reset all data to begin with
            self.ldb.load_players('data/challenger.csv')
            self.ldb.load_champions('data/champions.csv')
            self.ldb.load_match_history('data/match_history.csv')

    def test_get_player(self):
            self.reset_data()
            player = self.ldb.get_player() #insert acc_id
            self.assertEquals(player[0], 'Jumanji (1995)') #wins
            self.assertEquals(movie[1], 'Adventure|Children\'s|Fantasy') #losses
            self.assertEquals(movie[2], 'Adventure|Children\'s|Fantasy') #name
            self.assertEquals(movie[3], 'Adventure|Children\'s|Fantasy') #lp

    def test_get_player_null(self):
            self.reset_data()
            player = self.ldb.get_player(1337)
            self.assertEquals(player, None)

    def test_set_player(self):
            self.reset_data()
            player = self.ldb.get_player(acc_id) # insert acc_id
            player[0] = 'ABC'
            self.ldb.set_player(acc_id, player)
            player = self.ldb.get_player(acc_id)
            self.assertEquals(player[0], 'ABC')

    def test_delete_player(self):
            self.reset_data()
            self.ldb.delete_player() #acc_id
            player = self.ldb.get_player() #acc_id
            self.assertEquals(player, None)


    def test_get_champion(self):
            self.reset_data()
            champion = self.ldb.get_champion(3)
            self.assertEquals(champion[1], 25) #champion name
            self.assertEquals(champion[2], 15) #image

    def test_set_champion(self):
            self.reset_data()
            champion = self.ldb.get_champion(3)
            champion[2] = 6
            self.ldb.set_champion(3, champion)
            champion = self.ldb.get_champion(3)
            self.assertEquals(champion[1], 25)
            self.assertEquals(champion[2], 6)

    def test_delete_champion(self):
            self.reset_data()
            self.ldb.delete_champion(3)
            champion = self.ldb.get_champion(3)
            self.assertEquals(champion, None)


    def test_get_match_history(self):
            self.reset_data()
            match_history = self.ldb.get_match_history(32)
            self.assertEquals(match_history, 3.945731303772336)
            match_history = self.ldb.get_match_history(110)
            self.assertEquals(match_history, 4.234957020057307)
            match_history = self.ldb.get_match_history(1)
            self.assertEquals(match_history, 4.146846413095811)



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

