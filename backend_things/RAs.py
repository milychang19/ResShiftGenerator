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