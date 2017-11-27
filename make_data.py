##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# November 27, 2017
##############################


import csv
import json
import requests
import sys

N_GAMES		= 50000	 # The number of games to get data for
REGION		= 'na1'  # The North American region
API_KEY 	= 'RGAPI-63bd5919-e73d-4a66-ae0f-8f61803008be'
API_STR		= '?api_key=' + API_KEY
RIOT_URL	= 'https://' + REGION + '.api.riotgames.com/lol/'

CHALLENGER_IDS = []

# CSV FORMAT: wins(int),losses(int),playerOrTeamName(str),playerOrTeamId(str),leaguePoints(int)
def create_challenger_data():
	print('Creating challenger data...')
	
	# Create URL
	URL = RIOT_URL + 'league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5' + API_STR

	# Make request
	r = requests.get(URL)

	# Load data
	challenger_data = json.loads(r.content.decode('utf-8'))
	challenger_players = challenger_data['entries']

	# Write to CSV
	with open('data/challenger.csv', 'wb') as csvfile:
		w = csv.writer(csvfile, delimiter=',')
		for c in challenger_players:
			# Store challenger ID into list.
			CHALLENGER_IDS.append(int(c['playerOrTeamId'].encode('utf-8').rstrip()))
			# Write to CSV file.
			w.writerow([str(c['wins'])] + [str(c['losses'])] + [c['playerOrTeamName'].encode('utf-8')] + [c['playerOrTeamId'].encode('utf-8')] + [str(c['leaguePoints'])])

def create_match_history_data():
	print('Creating match history data...')

	pass

def create_match_data():
	print('Creating match data...')
	pass

def create_champion_data():
	print('Creating champion data...')
	pass

def create_item_data():
	print('Creating item data...')
	pass

if __name__ == '__main__':
	create_challenger_data()
	create_match_history_data()
	create_match_data()
	create_champion_data()
	create_item_data()

	sys.exit(0)

