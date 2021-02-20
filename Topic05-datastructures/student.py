# Stores a student's name and a list of her courses and grades in a dict. Prints out her data.

# Author: Cormac Hennigan

student = {"name": "Mary", "modules":[{"courseName": "Programming", "grade": 45}, {"courseName": "History",
 "grade": 99}]}

print ("Student: {}".format(student["name"]))

for module in student ["modules"]:
    print("\t {} \t {}".format(module["courseName"], module["grade"]))