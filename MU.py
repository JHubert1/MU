import sys
import numpy as np
import re
import csv

print("----\nWelcome to MU v1.1!\n----")
print("The Rules are simple: Let x,y be any string.\n1. xI -> xIU\n2. Mx -> Mxx\n3. xIIIy -> xUy\n4. xUUy -> xy")
print("Type one of the numbers to apply that rule. In case (3,4) specify which occurrence to use.\nE.g. MUUIUU, type '41' will result in MIUU, type '42' will result in MUUI.")
print("Type 'q' to exit (will save your work as a .txt!). Type 'h' for a reminder of the laws.\nHave fun!\n----")

Playing = True
string = "MI"
lawsused = ["0"]
strings = [string]

while(Playing):

    # Get input
    law = input(string+"\n")
    law=str(law)

    # Check input has 1 or 2 characters
    if(len(law) < 1 or len(law) > 2):
        print("Input not understood. "+law+"?")
        
    # Check that 2nd char is larger than 0
    elif(len(law)==2 and int(law[1])<= 0):
        print("Occurence is either 1 or more (integer). "+law+"?")

    # Exit
    elif(law[0] == "q"):
        stack = np.column_stack((lawsused,strings))
        with open("MU_Results.csv","w") as f:
            wr = csv.writer(f)
            wr.writerows(stack)
        sys.exit("See you.")

    # Law 1
    elif(law[0]=="1"):
        if(string[-1]!="I"):
            print("Can't apply this law!")
        else:
            string += "U"
            lawsused.append(law)
            strings.append(string)
    # Law 2
    elif(law[0]=="2"):
        string += string[1:]
        lawsused.append(law)
        strings.append(string)

    # Law 3
    elif(law[0]=="3"):
        matches = [(m.start(0), m.end(0)) for m in re.finditer("III", string)]
        if(len(law)==2 and (int(len(matches))<int(law[1]))):
            print("No occurrence there.")
        elif(len(law)==1):
            print("specify also which occurrence please.")
        else:
            start = matches[int(law[1])-1][0]
            end = matches[int(law[1])-1][1]
            string = string[:start]+"U"+string[end:]
            lawsused.append(law)
            strings.append(string)

    # Law 4
    elif(law[0]=="4"):
        matches = [(m.start(0), m.end(0)) for m in re.finditer("UU", string)]
        if(len(law)==2 and (int(len(matches))<int(law[1]))):
            print("No occurrence there.")
        elif(len(law)==1):
            print("specify also which occurrence please.")
        else:
            start = matches[int(law[1])-1][0]
            end = matches[int(law[1])-1][1]
            string = string[:start]+string[end:]
            lawsused.append(law)
            strings.append(string)
    # Help
    elif(law[0] == "h"):
        print("----\nLet x,y be any string.\n1. xI -> xIU\n2. Mx -> Mxx\n3. xIIIy -> xUy\n4. xUUy -> xy----\n")
    else:
        print("Input not understood: "+law+"?")
