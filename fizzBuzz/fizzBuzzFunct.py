import sys
sys.path.append("../calculator")
import calculator as calc

def setUp():
    usernum = float(raw_input("Please enter a number: "))
    return usernum

def fizz(num):
    modNum = calc.mod(num, 3)
    if modNum == 0:
        return "Fizz"
    else:
        return ""

def buzz(num):
    modNum = calc.mod(num, 5)
    if modNum == 0:
        return "Buzz"
    else:
        return ""

def finalPrint(fizz, buzz):
    print("{0} {1}".format(fizz, buzz))

def cleanUp(fizz, buzz):
    if fizz == "":
        if buzz != "":
            print buzz
    elif buzz == "":
        print fizz
    else:
        finalPrint(fizz, buzz)
