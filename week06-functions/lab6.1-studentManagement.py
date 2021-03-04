# Program that creates new students and views students
# Author: Cormac Hennigan

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

# choice = displayMenu()
# print("you chose {}".format(choice))

def doAdd():
    currentStudent = {}
    currentStudent["name"]=input("enter name : ")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit)").strip

def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))

def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

students= []
choice = displayMenu()
while (choice !="q"):
    if (choice == "a"):
        doAdd()
    elif (choice == "v"):
        doView()
    elif (choice != "q"):
        print("\n\nplease select either a,v or q")
    choice = displayMenu()
        
