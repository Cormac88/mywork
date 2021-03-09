import os.path
filename = "count.txt"
def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        # this file will be created when we write back.
        # no file assumes first time running
        # ie 0 previous runs 
        return 0

#num = readNumber()    # Test it
#print(num)          

def writeNumber(number):
    with open (filename, "wt") as f:
        f.write(str(number))    # write takes a string so we need to convert

# main
#num = readNumber()
#num += 1
#print ("we have run this program {} times".format(num))

import os.path
if not os.path.isfile(filename):
    print ("File does not exist")   #initialise file
    writeNumber(0)