import sys
sys.path.append("../calculator")
import calculator as calc

def setUp():
    print("Hi! I'm here to help you find out if your number is even or odd.")
    num = float(raw_input("Please enter a number here: "))
    return num

def evenOdd(num):
    modNum = calc.mod(num,2)
    if modNum == 0:
        print("{0} is even!".format(int(num)))
    elif modNum == 1:
        print("{0} is odd!".format(int(num)))
    else:
        print("{0} is neither even nor odd!".format(num))
