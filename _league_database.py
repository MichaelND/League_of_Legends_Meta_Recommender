##############################
# Anthony Luc, Michael Wang
# ParadigmsFinal
# November 27, 2017
##############################

class _league_database():
    def __init__(self):
        # stores the player's wins, losses, name, and lp based off of the account id
        self.players    = {}
        # stores the champion name and image based off of the champion key
        self.champions  = {}
        # stores the matches data
        self.matches    = {}
        # stores the champion data by meta and lane
        self.meta       = {}
        account_id      = 0
        champion_key    = 0

    def load_players(self, players_file):
        f = open(players_file, "r")
        for line in f:
            # store the data from the player file into dictionary

            values      = line.split(",")
            account_id  = int(values[3].rstrip('\n\r'))

            # Create input dictionary.
            p           = {}
            p['wins']   = int(values[0].rstrip('\n\r'))
            p['losses'] = int(values[1].rstrip('\n\r'))
            p['name']   = values[2].rstrip('\n\r')
            p['lp']     = int(values[4].rstrip('\n\r'))
            p['acc_id'] = account_id

            self.players[account_id] = p
        f.close()

    def load_champions(self, champions_file):
        f = open(champions_file, "r")
        for line in f:
            # store the data from the champions file into dictionary

            values              = line.split(",")
            champion_key        = int(values[1].rstrip('\n\r'))

            # Create input dictionary.
            c                   = {}
            c['c_name']         = values[0].rstrip('\n\r')
            c['image']          = values[2].rstrip('\n\r')
            c['lane']           = None

            self.champions[champion_key] = c
        f.close()

    def load_match_history(self, match_file):
        f = open(match_file, "r")
        for line in f:
            # store the data from the match_history file into dictionary

            values = line.split(",")
            account_id = int(values[0].rstrip('\n\r'))

            # Create input dictionary.
            m                   = {}
            m['lane']           = values[1].rstrip('\n\r')
            m['game_id']        = int(values[2].rstrip('\n\r'))
            m['champion_id']    = int(values[3].rstrip('\n\r'))
            m['queue']          = int(values[4].rstrip('\n\r'))
            m['role']           = values[5].rstrip('\n\r')
            m['timestamp']      = int(values[6].rstrip('\n\r'))

            try:
                self.matches[account_id].append(m)
            except KeyError:
                self.matches[account_id] = []
                self.matches[account_id].append(m)
        f.close()

    def get_player(self, account_id):
        retVal = {}
        try:
            retVal = self.players.get(int(account_id))
        except KeyError:
            retVal = None
        return retVal

    def get_champion(self, champion_key):
        retVal = {}
        try:
            retVal = self.champions.get(int(champion_key))
        except KeyError:
            retVal = None
        return retVal

    def get_match_history(self, account_id):
        retVal = {}
        try:
            retVal = self.matches.get(int(account_id))
        except KeyError:
            retVal = None
        return retVal

    def get_meta_rating(self, champion_name, lane):
        retVal = {}
        try:
            retVal = self.meta[lane].get(str(champion_name))
        except KeyError:
            retVal = None
        return retVal

    def set_player(self, account_id, data):
        account_id = int(account_id)
        if self.players.get(account_id) is None:
            self.players[account_id] = {}

        # Update data.
        self.players[account_id]['wins']        = data['wins']
        self.players[account_id]['losses']      = data['losses']
        self.players[account_id]['name']        = data['name']
        self.players[account_id]['lp']          = data['lp']
        self.players[account_id]['acc_id']      = account_id

    def set_champion(self, champion_key, data):
        champion_key = int(champion_key)
        if self.champions.get(champion_key) is None:
            self.champions[champion_key] = {}

        # Update data.
        self.champions[champion_key]['c_name']          = data['c_name']
        self.champions[champion_key]['image']           = data['image']

    def set_match_history(self, account_id, data, gameIdx):
        account_id = int(account_id)
        if self.matches.get(account_id) is None:
            self.matches[account_id] = {}

        # Update data.
        self.matches[account_id][gameIdx-1]['lane']         = data['lane']
        self.matches[account_id][gameIdx-1]['game_id']      = data['game_id']
        self.matches[account_id][gameIdx-1]['champion_id']  = data['champion_id']
        self.matches[account_id][gameIdx-1]['queue']        = data['queue']
        self.matches[account_id][gameIdx-1]['role']         = data['role']
        self.matches[account_id][gameIdx-1]['timestamp']    = data['timestamp']

    def delete_player(self, account_id):
        self.players.pop(int(account_id))

    def delete_champion(self, champion_key):
        self.champions.pop(int(champion_key))

    def delete_match_history(self, account_id):
        self.matches.pop(int(account_id))

    def delete_meta(self, champion_name):
        champion_name = str(champion_name)
        pop_list = []
        for k, v in self.meta.items():
            for champ, rating in v.items():
                if champ == champion_name:
                    pop_list.append([k,champ])

        # Loop through list and delete
        for tup in pop_list:
            self.meta[tup[0]].pop(tup[1])

    def delete_all_dictionaries(self):
        self.players    = {} 
        self.champions  = {}
        self.matches    = {}
        self.meta       = {}

    #- Advanced Functions -------------------------------------#
    def init_meta(self):
        self.meta['TOP']     = {}
        self.meta['JUNGLE']  = {}
        self.meta['MID']     = {}
        self.meta['BOTTOM']  = {}

        # Loop through all players and their matches.
        for acc_id, values in self.matches.items():
            # Loop through a player's matches
            for i in range(0, len(values)): 
                match = values[i]

                # Store champion indexed by lane
                lane = match['lane']
                game_id = match['game_id']

                # Get champion by champ id.
                champ_id = match['champion_id']
                try:
                    champion = self.champions[champ_id]

                    # Store indexing by lane.
                    try:
                        self.meta[lane][champion['c_name']] += 1  # increment meta counter
                    except:
                        self.meta[lane].update({champion['c_name'] : 1}) # Add to meta dictionary for the first time
                except KeyError as e:
                    continue

    def get_all_meta(self):
        ret_dict = {}

        for lane_key, lane_val_dict in self.meta.items():               # Loop through meta
            meta_list = [(k,v) for v,k in sorted([(v,k) for k,v in lane_val_dict.items()],reverse=True)]
            ret_dict.update({lane_key:meta_list[0:-1]})
        return ret_dict

    def get_n_meta(self, num):
        ret_dict = {}

        # Make sure num is positive and more than 0
        if num >= 0:
            for lane_key, lane_val_dict in self.meta.items():               # Loop through meta
                # Source: http://bytesizebio.net/2013/04/03/stupid-python-tricks-3296-sorting-a-dictionary-by-its-values/
                meta_list = [(k,v) for v,k in sorted([(v,k) for k,v in lane_val_dict.items()],reverse=True)]
                ret_dict.update({lane_key:meta_list[0:num]})
        return ret_dict

    def update_meta_vote(self, champion_name, lane, meta_vote):
        try:
            self.meta[lane][champion_name] += int(meta_vote)  # Update if in lane already
        except Exception as e:
            self.meta[lane].update({champion_name:1}) # Add to lane if not in
            print('Error' + str(e))
        return self.meta[lane][champion_name]


if __name__ == "__main__":
    ldb = _league_database()
    ldb.load_players('data/challenger_1m.csv')
    ldb.load_champions('data/champions_1m.csv')
    ldb.load_match_history('data/match_history_1m.csv')
    ldb.init_meta()

    # all_meta = ldb.get_all_meta()
    # print(all_meta)
    # n_meta = ldb.get_n_meta(2)
    # print(n_meta)

    # ldb.delete_meta('Kennen')
