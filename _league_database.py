##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# November 27, 2017
##############################

class _league_database():
	def __init__(self):
		# stores the player's wins, losses, name, and lp based off of the account id
		self.players 	= {} 
		# stores the champion name and image based off of the champion key
		self.champions 	= {} 
		# stores the user's input for whether a champion is meta
		self.matches 	= {}
		account_id 		= 0
		champion_key 	= 0

	def load_player(self, players_file):
		for line in open(players_file):
			# store the data from the player file into dictionary

			values 		= line.split(",")
			account_id 	= values[3].rstrip('\n')

			p 			= {}
			p['wins'] 	= int(values[0].rstrip('\n'))
			p['losses'] = int(values[1].rstrip('\n'))
			p['name'] 	= values[2].rstrip('\n')
			p['lp'] 	= int(values[4].rstrip('\n'))

			self.players[account_id] = p

	def load_champion(self, champions_file):
		for line in open(champions_file):
			# store the data from the player file into dictionary

			values 			= line.split(",")
			champion_key 	= values[1].rstrip('\n')

			c 				= {}
			c['c_name'] 	= values[0].rstrip('\n')
			c['image'] 		= values[2].rstrip('\n')

			self.champions[champion_key] = c

	def load_match_history(self, match_file):
		for line in open(match_file):
			# store the data from the player file into dictionary

			values = line.split(",")
			account_id = values[0].rstrip('\n')

			m 				= {}
			m['lane'] 		= values[1].rstrip('\n')
			m['gameId'] 	= values[2].rstrip('\n')
			m['champion'] 	= values[3].rstrip('\n')
			m['queue'] 		= values[4].rstrip('\n')
			m['role'] 		= values[5].rstrip('\n')
			m['timestamp'] 	= values[6].rstrip('\n')

			self.matches[account_id] = m

	def get_player(self, account_id):
		return self.players.get[account_id]

	def get_champion(self, champion_key):
		return self.champions.get[champion_key]

	def get_match_history(self, account_id):
		return self.match_history.get[account_id]

	def set_player(self, account_id, data):
		account_id = int(account_id)
		if self.players.get(account_id) is None:
			self.players[account_id] = {}

		self.players[account_id]['wins'] 	= data['wins']
		self.players[account_id]['losses'] 	= data['losses']
		self.players[account_id]['name'] 	= data['name']
		self.players[account_id]['lp'] 		= data['lp']

	def set_champion(self, champion_key, data):
		champion_key = int(champion_key)
		if self.champions.get(champion_key) is None:
			self.champions[champion_key] = {}

		self.champions[champion_key]['c_name']	= data['c_name']
		self.champions[champion_key]['image']	= data['image']

	def set_match_history(self, account_id, data):
		account_id = int(account_id)
		if self.matches.get(account_id) is None:
			self.matches[account_id] = {}

		self.matches[account_id]['lane'] 		= data['lane']
		self.matches[account_id]['gameId'] 		= data['gameId']
		self.matches[account_id]['champion'] 	= data['champion']
		self.matches[account_id]['queue'] 		= data['queue']
		self.matches[account_id]['role'] 		= data['role']
		self.matches[account_id]['timestamp'] 	= data['timestamp']

	def delete_player(self, account_id):
		self.players.pop(account_id)

	def delete_champion(self, champion_key):
		self.champions.pop(champion_key)

	def delete_match_history(self, account_id):
		self.matches.pop(account_id)

if __name__ == "__main__":
	ldb = _league_database()
	ldb.load_player('data/challenger.csv')
	ldb.load_champion('data/champions.csv')
	ldb.load_match_history('data/match_history.csv')

