import pandas as pd
import csv
import os

#gets CSV file from the filePath
#since it's going to be path/to/file/whatever.csv, we want to isolate the whatever.csv
def get_building_files(filePath):
    files_list = []
    count = 0
    for i in os.listdir(filePath):
        if ".csv" in i:
            # the string for the file will be "../whatever.csv"
            files_list.append(i[2:-4])
    if len(files_list) == 0:
        print("You have no files for any buildings")
    else:
        return files_list

#makes a list of dicts where the names of buildings are associated with None (as for now)
def print_file_list(print_list):
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
def set_building_team():
    #maybe add a password encryption for privacy
    print("What building team do you want to access?")
    print("Mountain (MNT)\tPrairie(PRA)\tMaritime (MAR)\tGordon Hall (GOR)")
    print("East Village Townhouses (EVH)\tEast Residence (EST)")
    print("Lennox-Addington (LAD)\tLambton/Watson (LWA)\tJohnston/Arts/Mills (JAM)")

    building = input(print("Building: "))

    #basically it will be like LAD.csv to access the LA team
    return building 



def get_building_team():

    path = "../buildings_CSV"
    lists_to_print = get_building_files(path)
    num_files = print_file_list(lists_to_print)
    team_file_name = set_building_team()

    #depending on what the csv files will be called, changes file path
    #now, it will be "../buildings_CSV/MNT.csv" 
    input_file_name = path + "/" + team_file_name + ".csv"
    print(input_file_name)
    open_file(input_file_name)

def first_pack_holder(io_file_name):
    num_first_pack_holder = []
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

def second_pack_holder(io_file_name):
    num_second_pack_holder = []
    try:
        with open(io_file_name) as csvDataFile:
            next(csvDataFile)
            csvReader = csv.reader(csvDataFile, delimiter = ',')
            for row in csvReader:
                #row[4] is amount of SH
                num_second_pack_holder.append(row[4])

    except:
        print("Error: file not found or opened properly")


#add all the values of all the shifts
def num_shifts():
    print("idk yet")

def open_file(io_file_name):
    staff_index = []
    try:
        with open(io_file_name) as csvDataFile:
            next(csvDataFile)
            csvReader = csv.reader(csvDataFile, delimiter = ',')
            for row in csvReader:
                #print(row)

                #row[0] indicates the index in the csv file so we can access staff better with dictionaries
                staff_index.append(row[0])

    except:
        print("Error: file not found or opened properly")
