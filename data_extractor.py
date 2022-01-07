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

    def __init__(self, summoner_name): 
        if not isinstance(summoner_name, str) and not summoner_name: 
            raise ValueError("Make sure summoner_name is a string")    
        self.summoner_name = summoner_name
        try: 
            self.puuid = self._retrieve_puuid()
            self.matches = self._retrieve_matches()
        except Exception as e: 
            raise e

    def _retrieve_puuid(self): 
        """
            retrieve a user's puuid
        """
        endpoint = PUUIS_ENDPOINT + self.summoner_name
        r = requests.get(endpoint, headers=HEADERS)
        json = r.json()
        return json["puuid"]
    
    def _retrieve_matches(self): 
        """
            retrieve a user's matches (ranked only ! )
        """
        endpoint = MATCHS_ENDPOINTS + f"{self.puuid}/ids?type=ranked"
        r = requests.get(endpoint, headers=HEADERS)
        return r.json()
         

class MatchDataExtractor: 
    """
        A class responsible for extracting a match informations
    """

    def __init__(self, match_id): 
        
        if not isinstance(match_id, str) and not match_id: 
            raise ValueError("Please make sure to provide a correct match_id")
        self.match_id = match_id 
        self.match_content = self.retrieve_match_content() 

    def _retrieve_match_content(self): 
        endpoint = MATCH_DETAIL_ENDPOINTS + self.match_id
        r = requests.get(endpoint, headers=HEADERS)
        return r.json()
        
