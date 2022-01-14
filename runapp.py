from extractor.extractor import UserDataExtractor, LeagueExtractor, MatchDataExtractor
from parser.parser import PlayerParser 
import os

PLAYER_CSV_PATH = os.path.join(
    os.path.join(os.getcwd(), "dataset"),
    "player.csv"
    )


def main(): 
    """
        entry point
    """

    
    
    league_extractor = LeagueExtractor()
    user_extract = UserDataExtractor()
    match_extractor = MatchDataExtractor() 
    player_parser = PlayerParser(filename=PLAYER_CSV_PATH)
    
    divisions = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINIUM", "DIAMOND"]
    tiers = range(1,4) 

    # is false if the player.csv has never been open before
    player_is_started = False 


    
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

                        for match_id in matches: 
                            
                            # retrieve match details
                            match_details = match_extractor.retrieve_match_content(match_id)
                            # extract related player information in the match
                            match_player_meta = player_parser.preprocess_content(match_details, puuid) 

                            data = {**player_payload, **match_player_meta} 
                            if not player_is_started: 
                                player_parser.write_into(data.keys())
                                player_is_started = True 
                            player_parser.flatten_and_write(data) 
                            break

                    break 

            break
            
        break
                


if __name__ == "__main__":
    main()