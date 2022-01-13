from urllib import response
import requests
from .constant import (PUUIS_ENDPOINT, HEADERS, MATCHS_ENDPOINTS, MATCH_DETAIL_ENDPOINTS,DIVISION_ENDPOINT)
import json
from .decorator import request # custom decorator




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
    
    @request
    def get_players(self, tier, division, page=1, queue="RANKED_SOLO_5x5"):
        """
            browse ranked players
        """
        endpoint = DIVISION_ENDPOINT + f"{queue}/{tier}/{self.tiers_list[division]}?page={page}"
        r = requests.get(endpoint, headers=HEADERS)
        return {
            "response" : r, 
            "endpoint" : endpoint
        }

    

class UserDataExtractor: 

    """
        A class responsible for the extracting a summoner related informations. 
        In short, instanciating this class will allow you to at least access summoner name and puuid
    """

    @request
    def retrieve_puuid(self, summoner_name): 
        """
            retrieve a user's puuid
        """
        endpoint = PUUIS_ENDPOINT + summoner_name
        r = requests.get(endpoint, headers=HEADERS)
        return {
            "response" : r, 
            "endpoint" : endpoint
        }


    @request
    def retrieve_matches(self, puuid): 
        """
            retrieve a user's matches (ranked only ! )
        """
        endpoint = MATCHS_ENDPOINTS + f"{puuid}/ids?type=ranked&start=0&count=50"
        r = requests.get(endpoint, headers=HEADERS)
        return {
            "response" : r, 
            "endpoint" : endpoint
        }



class MatchDataExtractor: 
    """
        A class responsible for extracting a match informations
    """
    
    @request
    def retrieve_match_content(self, match_id): 
        endpoint = MATCH_DETAIL_ENDPOINTS + match_id
        r = requests.get(endpoint, headers=HEADERS)
        return {
            "response" : r, 
            "endpoint" : endpoint
        }


