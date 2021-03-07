#Design and implement a Python program that is based on these requirements:
# a) define a class which has at least two methods
# o	Method 1 – getString: to get a string from console input; and,
# o	Method 2 - printString: to print the string in upper case.
# b) demonstrate code works using three different test input strings

#defintes relay class with default constuctor taking no args
class relay:
    def __init__(self):
        #instance var: intake is an empty string
        self.intake = ''

    def getString(self):
        #reassigns instance var to return of input()
        self.intake = input()
    def printString(self):
        #relays instance variable via print method
        print(self.intake)

#demonstration
# test_conditions:'abcdefghijk' 'ABCDEFGHIJK' 'aAbBcCdDeEfFgGhHiIjJkK'

listner = relay()
listner.getString()
listner.printString()
