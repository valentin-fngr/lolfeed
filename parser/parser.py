from abc import abstractclassmethod, abstractmethod
import csv
from fileinput import filename
from abc import ABC, abstractmethod


class CsvWritterMixin(ABC): 

    @abstractmethod
    def preprocess_content(self, content): 
        pass



class BaseCsvWritter: 

    def __init__(self, filename): 
        self.filename = filename

    
    def get_columns(self): 
        with open(filename) as csvfile: 
            file = csv.reader(csvfile, delimiter=",") 
            for row in file: 
                return ", ".join(row)


    def write_into(self, row): 
        """
            add a column of the preprocessed row into filename 
            note : row is a list
        """
        with open(self.filename, 'a+', newline='') as csvfile:
            current_file = csv.writer(csvfile, delimiter=",") 
            current_file.writerow(row)

        print("successfully wrote to ", self.filename)

        

    def flatten_and_write(self, row): 
        """
            return the values of a the content dictionarry and writes it to the file
        """
        return self.write_into(row.values())
        
        

class PlayerParser(CsvWritterMixin, BaseCsvWritter): 
     
    def __init__(self, filename):
        super().__init__(filename)

    def get_columns(self):
        return super().get_columns()

    def write_into(self, row):
        return super().write_into(row)

    def flatten_and_write(self, row): 
        """
            return the values of a the content dictionarry and writes it to the file
        """
        return super().flatten_and_write(row)

    def preprocess_content(self, match_content, user_puuid):
        """
            Return the user match info by its puuid, as a dictionnary 
            Argument: 
                content : a match payload, 
                user_puuid
        """

        data = {}
        participants = match_content["info"]["participants"]
        for participant in participants: 
            if participant["puuid"] == user_puuid: 
                # extract 
                data["champExperience"] = participant["champExperience"]
                data["champLevel"] = participant["champLevel"]
                data["championName"] = participant["championName"] 
                data["damageDealtToBuildings"] = participant["damageDealtToBuildings"] 
                data["damageDealtToObjectives"] = participant["damageDealtToObjectives"] 
                data["damageDealtToTurrets"] = participant["damageDealtToTurrets"] 
                data["kills"] = participant["kills"]                
                data["deaths"] = participant["deaths"] 
                data["assists"] = participant["assists"]
                data["detectorWardsPlaced"] = participant["detectorWardsPlaced"] 
                data["doubleKills"] = participant["doubleKills"] 
                data["dragonKills"] = participant["dragonKills"] 
                data["firstTowerKill"] = participant["firstTowerKill"] 
                data["firstTowerAssist"] = participant["firstTowerAssist"]
                data["firstBloodAssist"] = participant["firstBloodAssist"] 
                data["firstBloodKill"] = participant["firstBloodKill"]
                data["goldEarned"] = participant["goldEarned"] 
                data["individualPosition"] = participant["individualPosition"] 
                data["magicDamageDealt"] = participant["magicDamageDealt"] 
                data["pentaKills"] = participant["pentaKills"] 
                data["quadraKills"] = participant["quadraKills"]
                data["killingSprees"] = participant["killingSprees"] 
                data["physicalDamageDealtToChampions"] = participant["physicalDamageDealtToChampions"] 
                data["physicalDamageTaken"] = participant["physicalDamageTaken"]
                data["totalDamageDealtToChampions"] = participant["totalDamageDealtToChampions"] 
                data["totalDamageShieldedOnTeammates"] = participant["totalDamageShieldedOnTeammates"]
                data["totalDamageTaken"] = participant["totalDamageTaken"]
                data["totalHeal"] = participant["totalHeal"]
                data["tripleKills"] = participant["tripleKills"]
                data["visionScore"] = participant["visionScore"]
                data["wardsPlaced"] = participant["wardsPlaced"]
                data["totalMinionsKilled"] = participant["totalMinionsKilled"]
                data["win"] = participant["win"]

                return data
        return None


class MatchParser(CsvWritterMixin, BaseCsvWritter): 
    def __init__(self, filename):
        super().__init__(filename)


    def preprocess_content(self, match_content):
        """
            extract relevant match data 
        """
        data = {}
        meta = match_content["metadata"]
        info = match_content["info"]
        data["matchId"] = meta["matchId"]  
        data["game_id"] = info["gameId"]
        data["gameDuration"] = info["gameDuration"]
        data["gameMode"] = info["gameMode"]
        data["gameCreation"] = info["gameCreation"] 

        return data        

    def is_in_csv(self, matchId): 
        """
            return true if the match has already been written in the csv 
            in order to avoid duplicates
        """
        # counter allows us to avoid checking the first row, which contains the name of each column
        counter = 0
        with open(self.filename, newline='') as csvfile:
            file_content = csv.reader(csvfile, delimiter=",") 
            for row in file_content: 
                if counter != 0: 
                    if row[0] == matchId: 
                        return True 
        return False
