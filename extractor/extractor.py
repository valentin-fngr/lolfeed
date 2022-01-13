import requests
from .constant import (PUUIS_ENDPOINT, HEADERS, MATCHS_ENDPOINTS, MATCH_DETAIL_ENDPOINTS,DIVISION_ENDPOINT)
import json

"""
Interact with the riot API in order to retrieve match and user data, in order to store them in a db later
"""



class LeagueExtractor: 

    """
        A class that aims at extracting players
    """

    def __init__(self): 

        self.tiers_list = {
            "1": "I", 
            "2" : "II", 
            "3" : "III", 
            "4" : "IV"
        }

        self.division_list = ["IRON", "BRONZE", "SILVER", "GOLD", "PLATINIUM", "DIAMOND"]
    

    def get_players(self, tier, division, page=1, queue="RANKED_SOLO_5x5"):

        endpoint = DIVISION_ENDPOINT + f"{queue}/{tier}/{self.tiers_list[division]}?page={page}"
        r = requests.get(endpoint, headers=HEADERS)
        content = r.json()

        print(content)

        if r.status_code != 202:
            msg = content["status"]["message"]
            print(f"WARNING : request {endpoint} failed with status {r.status_code}")
            print(f"WARNING : request failed because : {msg}")
            
            return None
        return content   

    

class UserDataExtractor: 

    """
        A class responsible for the extracting a summoner related informations. 
        In short, instanciating this class will allow you to at least access summoner name and puuid
    """

    def retrieve_puuid(self, summoner_name): 
        """
            retrieve a user's puuid
        """
        endpoint = PUUIS_ENDPOINT + summoner_name
        r = requests.get(endpoint, headers=HEADERS)
        json = r.json()

        if r.status_code == 202:  
            return r.json()      
        else: 
            return None       

    def retrieve_matches(self, puuid): 
        """
            retrieve a user's matches (ranked only ! )
        """
        endpoint = MATCHS_ENDPOINTS + f"{puuid}/ids?type=ranked"
        r = requests.get(endpoint, headers=HEADERS)

        if r.status_code == 202:  
            return r.json()      
        else: 
            return None   


         

class MatchDataExtractor: 
    """
        A class responsible for extracting a match informations
    """
    
    def retrieve_match_content(self, match_id): 
        endpoint = MATCH_DETAIL_ENDPOINTS + match_id
        r = requests.get(endpoint, headers=HEADERS)

        if r.status_code == 202:  
            return r.json()      
        else: 
            return None           
