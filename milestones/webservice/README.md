Programmers: Anthony Luc, Michael Wang
Project: Paradigms Final Project
Date: November 27, 2017


## Milestone 2
For this project, we will use League of Legends's API to gather data which will allow users to use our API to vote on which champions they believe are meta for the current season. From the Riot API, we will use our own script to parse data from the top 200 challenger players by their summoner names and then use that data to go through their each of their past 20 games in their match history to see which champions they played. There are three different data files that our scripts generate from the League of Legends Api and they include champions.csv, match_history.csv, and challenger.csv. Champions.csv contains all of the champions and their key. Match_history.csv contains the most recent 20 matches for the top 200 challenger players and which champions they played. Challenger.csv contains the top 200 challenger players and their account info. 

One thing to note is that our scripts use a generated api key from Riot Games which will expire in two days so there is a possibility that the script to generate the .csv files will not work and will need new api keys. 

Our OO API's main feature will be for the users to be able to see what champions the best league of legends players are currently playing and be able to vote for and get what champions are in the meta based off of our databases. 

To test our OO API for November 27, simply run python3 test_api.py. This will test our load, get, set, and delete functions for our league database class. 

A link to our GitHub is provided here as well: https://github.com/MichaelND/ParadigmsFinal

## Milestone 3
We are using port number 51049 for our webservice. The user will be able to use our webservice to obtain information about champions, players, matches, and also the meta. For the players side, a user can send a get request to the webservice with and without a key to specify a challenger player based on their account id or all the challenger players information. The user can post a new challenger player to the webservice if a new player were to enter challenger for example. In addition when a player falls out of challenger, the user can delete the challenger player by sending a delete request with the account id as the key. The user can also obtain the match history information of all the challenger players by making a get request or a specific challenger player with a get request with the account id. Let's say that a challenger player plays a new match and the user wants to record that information. They can by making a post request! In addition, you can only have 20 matches in the match history so a user can then delete a match by sending a delete request to the webservice. The user has access to the database if they want to retrieve champions and also update an existing champion. Ultimately, the user will be able to vote on a champion based on whether they think it is meta and then get what champions are meta based on a certain lane or for everylane. The user will be able to learn more about what champions are best or most winning in challenger for each lane and then constantly be updated by the challenger players as they play matches. 

Note: We are currently in progress for adding the meta last feature for our webservice where the meta data can be pulled from. This is because we weren't sure whether this milestone allowed for us to update our object oriented api and so we added the webservice side to our previous existing object oriented api and these features are being tested for this milestone. 

Ultimately, we want our webservice to improve player's awareness about the current meta based off of challenger players by making get requests and also updates of their own to our webservice. On top of this features, the user will be able to obtain interact with and obtain information and match history about challenger league players as well as different champions. 

To test our webservice for November 30, simply run python3 test_ws.py. This will send multiple get, put, post, and delete requests to our webservice to show that it works.

A link to our GitHub is provided here as well: https://github.com/MichaelND/ParadigmsFinal
