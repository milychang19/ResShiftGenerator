import pandas as pd
import csv
import os

class FileManager:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.staff_df = None

    #gets CSV file from the filePath
    #since it's going to be path/to/file/whatever.csv, we want to isolate the whatever.csv
    def get_building_files(self):
        files_list = []
        count = 0
        for i in os.listdir(self.csv_path):
            if i.endswith(".csv"):
                # the string for the file will be "../whatever.csv"
                files_list.append(i[2:-4])
        if len(files_list) == 0:
            print("You have no files for any buildings")
        else:
            #the list of the files
            return files_list


    #makes a list of dicts where the names of buildings are associated with None (as for now)
    def print_files_list(print_list):
        if len(print_list) == 0:
            print("You have no files for any buildings")    
        else: 
            count = 1
            num_lists = []
            print("These are the building teams available: ")
            print_list = list(dict.fromkeys(print_list))
            #iterate through the list of files
            for i in print_list:
                print(f"{count}) {i}")
                print_list.append(str(count))
                count += 1
            return print_list

    #asks for building name and would set the building of which the employees would be associated w/    
    def set_building_team(self):
        #maybe add a password encryption for privacy
        print("What building team do you want to access?")
        print("Mountain (MNT)\tPrairie(PRA)\tMaritime (MAR)\tGordon Hall (GOR)")
        print("East Village Townhouses (EVH)\tEast Residence (EST)")
        print("Lennox-Addington (LAD)\tLambton/Watson (LWA)\tJohnston/Arts/Mills (JAM)")

        building = input(print("Building: "))

        #basically it will be like LAD.csv to access the LA team
        return building 



    def get_building_team(self):
        path = "../buildings_CSV"
        lists_to_print = self.get_building_files()
        team_file_name = self.set_building_team()
        input_file_name = os.path.join(self.csv_path, f"{team_file_name}.csv")

        #depending on what the csv files will be called, changes file path
        #now, it will be "../buildings_CSV/MNT.csv" 
        #input_file_name = path + "/" + team_file_name + ".csv"
        return input_file_name
        
    def open_file(self, io_file_name):
        try:
            self.staff_df = pd.read_csv(io_file_name)
            return self.staff_df
        except FileNotFoundError:
            print("Error: file not found or opened properly")
        except Exception as e:
            print(f"Error: {e}")
    
    def get_df(self):
        return self.staff_df

    def get_column(self, column_name):
        return self.staff_df[column_name]

    def get_first_pack_holder(self):
        return self.get_column('First Pack Holder')

    def get_second_pack_holder(self):
        return self.get_column('Second Pack Holder')

    def get_first_pack_non(self):
        return self.get_column('First Pack')

    def get_second_pack_non(self):
        return self.get_column('Second Pack')

    def get_backup(self):
        return self.get_column('Backup')

    def set_total(self):
        self.staff_df["Total_shifts"] = self.staff_df['Second Pack Holder'] + self.staff_df['First Pack'] + self.staff_df['Second Pack'] + self.staff_df['Backup']

staff_data = FileManager("../teamInfo.csv")



'''
    def other():
        num = staff_df[staff_df['PH'] > 3]
        try:
            with open(io_file_name) as csvDataFile:
                next(csvDataFile)
                csvReader = csv.reader(csvDataFile, delimiter = ',')
                for row in csvReader:
                    #row[3] is amount of FH
                    num_first_pack_holder.append(row[3])
            num = staff_df[staff_df['PH'] > 3]
        except:
            print("Error: file not found or opened properly")



    #add all the values of all the shifts
    def num_shifts():
        ph
'''

class RAs: # Better names: ResAssist, RAProfile, RAInfo
    # Constructor
    def __init__(self, stuID, name, shifts):
        self.empID = stuID
        self.RAname = name
        self.numShifts = shifts

    # Dictionary
    def display(self, employee):
        print(employee.__dict__)

    def get_RA_name(self, value):
        self.value = value

obj = RAs(1234, "Bruce", {"FH":1, "SH":3,"FN":3,"SN":2})
#print(obj.__dict__)
obj.display(obj)

# workers = ["kelly", "eve", "brad"]
# for worker in workers:
#     if 
# print(p.empID)
# print(p.RAname)

FH_worked = []

#values from the SQL dataebase to implement later on
# RA_dict = {
#     "12345":{'i':0,
#                 "name":"richard",
#                 "FH":1, 
#                 "SH":3,
#                 "FN":3,
#                 "SN":2},
#     "56789":{'i':1,
#                 "name":"emily",
#                 "FH":3, 
#                 "SH":1,
#                 "FN":2,
#                 "SN":4},
#     "24789":{'i':2,
#                 "name":"milky",
#                 "FH":2, 
#                 "SH":1,
#                 "FN":3,
#                 "SN":4}
# }
# print(RA_dict["56789"]["name"], RA_dict["56789"]["SN"])

#for i in 