import calculator as calc

try:
    (num1, op, num2) = calc.askForNums()

    if op == "+":
        finalNum = calc.add(num1, num2)
        calc.finalPrint(num1, op, num2, finalNum)
    elif op == "-":
        finalNum = calc.subtract(num1, num2)
        calc.finalPrint(num1, op, num2, finalNum)
    elif op == "*":
        finalNum = calc.multiply(num1, num2)
        calc.finalPrint(num1, op, num2, finalNum)
    elif op == "/":
        finalNum = calc.divide(num1, num2)
        calc.finalPrint(num1, op, num2, finalNum)
    elif op == "%":
        finalNum = calc.mod(num1, num2)
        calc.finalPrint(num1, op, num2, finalNum)
    else:
        print("Please use an operator that is in the parenthesis.")



except ValueError:
    print("Please only inpt valid numerical quantities and operators.")
