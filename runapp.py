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

                    player_payload = {
                        "wins" : player["wins"], 
                        "losses" : player["losses"], 
                        "inactive" : player["inactive"], 
                        "hotStreak" : player["hotStreak"], 
                        "tier" : player["tier"], 
                        "rank" : player["rank"]
                    }

                
                    summoner_name = player["summonerName"]

                    puuid = user_extract.retrieve_puuid(summoner_name)["puuid"]
                    
                    player_payload["puuid"] = puuid

                    # TODO : add to the database !
                    matches = user_extract.retrieve_matches(puuid) 
                    
                    if matches is not None: 

                        for match in matches: 
                            match_data = match_extractor.retrieve_match_content(match)
                            




                            break

                    break 

            break
            
        break
                


if __name__ == "__main__":
    main()