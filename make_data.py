##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# November 27, 2017
##############################


import csv
import json
import requests
import sys
import time

N_GAMES			= 10	# The number of games to get data
N_CHALL_PLAYER	= 200		# Number of challenger players
N_GAMES_PLAYER	= N_GAMES / N_CHALL_PLAYER	 # The number of games to get data for per player
REGION			= 'na1'  # The North American region
API_KEY 		= 'RGAPI-6599323f-b31d-4309-a76e-aa9f84fb0469'
API_STR			= '?api_key=' + API_KEY
RIOT_URL		= 'https://' + REGION + '.api.riotgames.com/lol/'

CHALLENGER_NAMES 	= []
CHALLENGER_ACC_IDS	= {}


# Turn string to bytes
def stob(string):
	return string.encode(string)

def make_requests(URL):
	# Make request.
	r = requests.get(URL)
	if r.status_code != 200:
		print("Status Code = " + str(r.status_code))
		while r.status_code != 200:
			if r.status_code == 429:  # Limit has been reached
				print('Limit has been reached. Sleeping...')
				time.sleep(121)
			r = requests.get(URL)  # Remake request

	return r


# CSV FORMAT: wins(int),losses(int),playerOrTeamName(str),account_id(int),leaguePoints(int)
def create_challenger_data():
	print('Creating challenger data...')
	
	# First find players in Challenger ###

	# Create URL.
	URL = RIOT_URL + 'league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5' + API_STR

	# Make request.
	r = make_requests(URL)

	# Load data.
	challenger_tier_data = json.loads(r.content.decode('utf-8'))
	challenger_players = challenger_tier_data['entries']
	for c in challenger_players:
		# Store challenger ID into list.
		CHALLENGER_NAMES.append(c['playerOrTeamName'].encode('utf-8').rstrip())

	# Next find challenger player account id ###
	for n in CHALLENGER_NAMES:
		n = n.decode('utf-8')
		print(n)
		# Create URL
		URL = RIOT_URL + 'summoner/v3/summoners/by-name/' + n + API_STR

		# Make request.
		r = make_requests(URL)

		# Load data
		data = json.loads(r.content.decode('utf-8'))

		# Append id to list.
		CHALLENGER_ACC_IDS[n] = str(data['accountId'])

	# Write to CSV.
	with open('data/challenger_1m.csv', 'wb') as csvfile:
		w = csv.writer(csvfile, delimiter=',')
		for c in challenger_players:
			n = c['playerOrTeamName'].rstrip()
			c_id = CHALLENGER_ACC_IDS[n]  # Get ID

			# Write to CSV file.
			print(type(c['wins']))
			print(type(c['losses']))
			print(type(n))
			print(type(c_id))
			print(type(c['leaguePoints']))
			w.writerow([c['wins']] + [c['losses']] + [stob(n)] + [c_id] + [c['leaguePoints']])


# DEPRECATED
# CSV FORMAT: acc_id(int),lane(str),gameId(long),champion(int),queue(int),role(str),timestamp(long)
# Recent is recent 20 games.
def create_recent_match_history_data():
	print('Creating recent match history data...')

	# MANUAL CHANGE: If Challenger csv has been made.
	with open('data/challenger_1m.csv', 'rb') as csvfile:
		r = csv.reader(csvfile, delimiter=',')
		for row in r:
			CHALLENGER_ACC_IDS[row[2]] = row[3]

	# Write to CSV.
	with open('data/recent_match_history_1m.csv', 'wb') as csvfile:
		w = csv.writer(csvfile, delimiter=',')

		# Loop through challenger ids.
		for c_acc_name, c_acc_id in CHALLENGER_ACC_IDS.items():
			# Create URL.
			URL = RIOT_URL + 'match/v3/matchlists/by-account/' + str(c_acc_id) + '/recent' + API_STR

			# Make request.
			r = make_requests(URL)

			# Load data.
			match_history_data = json.loads(r.content.decode('utf-8'))
			recent_matches = match_history_data['matches']

			# Loop through games.
			for i in range(len(recent_matches)):
				w.writerow([c_acc_id] + [recent_matches[i]['lane']] + [str(recent_matches[i]['gameId'])] + [str(recent_matches[i]['champion'])] + [str(recent_matches[i]['queue'])] + [recent_matches[i]['role']] + [str(recent_matches[i]['timestamp'])])


# CSV FORMAT: acc_id(int),lane(str),gameId(long),champion(int),queue(int),role(str),timestamp(long)
def create_match_history_data():
	print('Creating match history data...')

	# # MANUAL CHANGE: If Challenger csv has been made.
	# with open('data/challenger_1m.csv', 'rb') as csvfile:
	# 	r = csv.reader(csvfile, delimiter=',')
	# 	for row in r:
	# 		CHALLENGER_ACC_IDS[row[2]] = row[3]

	# Write to CSV.
	with open('data/match_history_1m.csv', 'wb') as csvfile:
		w = csv.writer(csvfile, delimiter=',')

		# Loop through challenger ids.
		for c_acc_name, c_acc_id in CHALLENGER_ACC_IDS.items():
			# Create URL.
			URL = RIOT_URL + 'match/v3/matchlists/by-account/' + str(c_acc_id) + API_STR

			# Make request.
			r = make_requests(URL)

			# Load data.
			match_history_data = json.loads(r.content.decode('utf-8'))
			matches = match_history_data['matches']

			# Loop through games.
			solo_count = 0
			for i in range(len(matches)):
				# Check if game is a soloqueue game.
				while solo_count < N_GAMES_PLAYER:
					if matches[i]['queue'] == 420:
						w.writerow([c_acc_id] + [matches[i]['lane']] + [str(matches[i]['gameId'])] + [str(matches[i]['champion'])] + [str(matches[i]['queue'])] + [matches[i]['role']] + [str(matches[i]['timestamp'])])



# CSV FORMAT: champion_name(str),key(int),image_name(str)
def create_champion_data():
	print('Creating champion data...')

	# Create URL
	URL = 'https://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json'

	# Make request.
	r = make_requests(URL)

	# Load data
	data = json.loads(r.content.decode('utf-8'))
	champions = data['data'].keys()

	# Write to CSV
	with open('data/champions_1m.csv', 'wb') as csvfile:
		w = csv.writer(csvfile, delimiter=',')
		for c in champions:
			# Write to CSV file.
			w.writerow( [c] + [data['data'][c]['key']] + [data['data'][c]['image']['full']])


if __name__ == '__main__':
	create_challenger_data()
	create_match_history_data()
	# create_recent_match_history_data() # calls the api for 20
	create_champion_data()

	sys.exit(0)

