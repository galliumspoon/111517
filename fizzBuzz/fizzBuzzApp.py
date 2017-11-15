import fizzBuzzFunct as fb

try:
    num = fb.setUp()
    fizz = fb.fizz(num)
    buzz = fb.buzz(num)
    fb.cleanUp(fizz, buzz)

except ValueError:
    print("Please input numbers only.")
