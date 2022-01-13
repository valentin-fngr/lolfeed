import requests
from .constant import (PUUIS_ENDPOINT, HEADERS, MATCHS_ENDPOINTS, MATCH_DETAIL_ENDPOINTS)


"""
Interact with the riot API in order to retrieve match and user data, in order to store them in a db later
"""



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
        return json["puuid"]
    
    def retrieve_matches(self, puuid): 
        """
            retrieve a user's matches (ranked only ! )
        """
        endpoint = MATCHS_ENDPOINTS + f"{puuid}/ids?type=ranked"
        r = requests.get(endpoint, headers=HEADERS)
        return r.json()
         

class MatchDataExtractor: 
    """
        A class responsible for extracting a match informations
    """
    
    def retrieve_match_content(self, match_id): 
        endpoint = MATCH_DETAIL_ENDPOINTS + match_id
        r = requests.get(endpoint, headers=HEADERS)
        return r.json()
        
