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
TODO
