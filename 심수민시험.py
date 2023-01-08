from datetime import datetime 
import sys

global chance
chance=4
def inputDay(str):
    global chance
    while True:
        if (chance<1):
            print("Too many attempts of entering inputs\nProgram terminated ...")
            break
        while True:
            if (chance <1):
                break
            month=int(input(f"{str}: Enter month born (1-12): "))
            if ((month>12 or month<1)and chance>=0):
                print("Invalid month, Please reenter")
                chance-=1
            else:
                break
        if(chance==0):
            continue

        while True:
            if (chance <1):
                break
            day=int(input(f"{str}: Enter day born (1-31): "))
            if ((day>31 or day<1)and chance>=0):
                print("Invalid day, Please reenter")
                chance-=1
            else:
                break
        if(chance==0):
            continue

        while True:
            if (chance <1):
                break
            year=int(input(f"{str}: Enter year born (4-digit): "))
            if ((year>9999 or year<1000)and chance>=0):
                print("Invalid year, Please reenter")
                chance-=1
            else:
                break
        if(chance==0):
            continue

        try:
            returnday=datetime(year,month,day)
            return returnday
        except:
            print("Day is out of range for month")
            print("Program terminated ...")
            sys.exit(1)

bornDay=inputDay("You ")

if (chance>0):
    Today=inputDay("Today ")

if (chance>0):

        if (bornDay == Today):
            print ("Number of days you lived: 0")
        elif (bornDay > Today):
                print("Birthdate should be less than the current date\nProgram terminated ...")
        else :
            print("Number of days you lived: ", (Today-bornDay).days)

