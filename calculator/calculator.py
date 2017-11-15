def askForNums():
    print("I'm here to help solve math problems!")
    num1 = float(raw_input("Give me your first number: "))
    op = raw_input("Give me an operator: (+,-,*,/) ")
    num2 = float(raw_input("Give me your second number: "))
    return num1, op, num2

def add(num1, num2):
    finalNum = num1 + num2
    return finalNum

def subtract(num1, num2):
    finalNum = num1 - num2
    return finalNum

def multiply(num1, num2):
    finalNum = num1 * num2
    return finalNum

def divide(num1, num2):
    finalNum = num1 / num2
    return finalNum

def mod(num1, num2):
    finalNum = num1 % num2
    return finalNum

def finalPrint(num1, op, num2, finalNum):
    print ("The result of {0} {1} {2} is {3}.".format(num1,op,num2,finalNum))
