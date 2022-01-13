from extractor.extractor import UserDataExtractor, LeagueExtractor, MatchDataExtractor


def main(): 
    """
        entry point
    """
    
    league_extractor = LeagueExtractor()
    user_extract = UserDataExtractor()
    match_extractor = MatchDataExtractor() 
    
    divisions = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINIUM", "DIAMOND"]
    tiers = range(1,4) 

    
    # iterating over all divisions, tiers 
    for i in range(len(divisions)): 
        for j in range(len(tiers)): 
            
            players = league_extractor.get_players(divisions[0], str(tiers[0]))
            
            # extracting each player'ids 
            if players: 
                for player in players:
                    summoner_name = player["summonerName"]

                    puuid = user_extract.retrieve_puuid(summoner_name) 
                    matches = user_extract.retrieve_matches(puuid) 
                        
                


if __name__ == "__main__":
    main()