import csv
from fileinput import filename



class CsvWritter: 

    def __init__(self, filename): 
        self.filename = filename

    
    def get_columns(self): 
        with open(filename) as csvfile: 
            file = csv.reader(csvfile, delimiter=",") 
            for row in file: 
                return ", ".join(row)


    def write_into(self, filename, content): 
        """
            add a column of the preprocessed content into filename 
            note : content is a list
        """
        with open(filename, 'w', newline='') as csvfile:
            current_file = csv.writer(csvfile, delimiter=",") 
            current_file.writerow(content)
        
        

class PlayerWritter(CsvWritter): 
     
    def __init__(self, filename):
        super().__init__(filename)

    def get_columns(self):
        return super().get_columns()



    def write_into(self, filename, content):
        return super().write_into(filename, content)

