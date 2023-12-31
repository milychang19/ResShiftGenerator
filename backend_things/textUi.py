from calendarDS import calendarDS

print("Choose a team building")
print("1. JAM (Johnston Artz Haus Mills)")
print("2. LAWA (Lampton Watson)")
print("3. LA (Lennox Addington)")
print("4. East Village")
print("5. East Towers")
print("6. Mountain")
print("7. Pairie")
print("8. Maritime")
print("9. Gordon Hall")
building = int (input("Enter a number: "))

def selectTeam(team): 
    # Need to add more actions when a team is selected
    if building == 1:
        return "JAM (Johnston Artz Haus Mills)"
    elif building == 2:
        return "LAWA (Lampton Watson)"
    elif building == 3:
        return "LA (Lennox Addington)"
    elif building == 4:
        return "East Village"
    elif building == 5:
        return "East Towers"
    elif building == 6:
        return "Mountain"
    elif building == 7:
        return "Pairie"
    elif building == 8:
        return "Maritime"
    elif building == 9:
        return "Gordon Hall"
    else:
        return "This number is not valid"

print("You've selected", selectTeam(building), "team")

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
# new object myCalendar
myCalendar = calendarDS(5,year,month)
# Add more actions when a month is selected
calendarDS.printCalendar(year, month)

print("We're only assuming 2 packs for now, one pack holder and one non pack holder")
print("everyone can have three days off(with priority)")

print(selectTeam(building), "Team: ")
# need a method in other file that output the whole team
print("Select a member or 0 once you're done")
# crunching algorithm ~ ~ ~ ~ ~ ~ ~~  ~ ~~ ~ ~ ~
# print the result