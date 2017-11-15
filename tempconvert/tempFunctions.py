def celstofaren(temp):
    finalTemp = temp * 1.8 + 32
    return finalTemp

def farentocels(temp):
    finalTemp = (temp - 32) * .5556
    return finalTemp

def display(temp):
    if temp.lower() == "f":
        tempToConvert = float(raw_input("Enter a temperature to convert to Farenheit: "))
        finalTemp = celstofaren(tempToConvert)
        print("{0} degrees Celsius is {1} degrees Farenheit.".format(tempToConvert, finalTemp))
    elif temp.lower() == "c":
        tempToConvert = float(raw_input("Enter a temperature to convert to Celsius: "))
        finalTemp = farentocels(tempToConvert)
        print("{0} degrees Farenheit is {1} degrees Celsius.".format(tempToConvert, finalTemp))
    else:
        print('Please just put "c" or "f".')
