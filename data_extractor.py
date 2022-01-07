import requests
from .constant import (PUUIS_ENDPOINT, HEADERS)


"""
Interact with the riot API in order to retrieve match and user data, in order to store them in a db later
"""



class UserDataExtractor: 

    """
        A class responsible for the extracting a summoner related informations. 
        In short, instanciating this class will allow you to at least access summoner name and puuid
    """

    def __init__(self, summoner_name): 
        if not isinstance(summoner_name, str): 
            raise ValueError("Make sure summoner_name is a string")    
        self.summoner_name = summoner_name
        self.puuid = self.retrieve_puuid()
    

    def retrieve_puuid(self): 
        """
            retrieve a user's puuid
        """
        endpoint = PUUIS_ENDPOINT + self.summoner_name
        r = requests.get(endpoint, headers=HEADERS)
        json = r.json()
        return json["puuid"]
    

    

