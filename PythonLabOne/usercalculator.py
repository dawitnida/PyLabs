'''Development of Web Applications and Web Services
    Assignment 1- Python, Exercise 2

    This program calculates the average number from a List and display result fetched from dictionary object,
    Update the program in 'simplecalculator.py', such that it takes a string of mixed letters and numbers
    from the user, parse out numbers from it and initialize the class object.
'''

__author__ = "Dawit Nida (dawit.nida@abo.fi)"
__date__ = "Date: 10.9.2014"
__version__ = "Version: "

import re

class AverageCalculator():
    def __init__(self, numList):
        self.numList = numList
     # imp! @classmethod DECORATOR Method DO: accept user input from the terminal
    @classmethod
    def process_user_input(self):
        terminal_input = raw_input("Enter string ...")
        return terminal_input
    # extract a list of numbers and initialize the object, parse out numbers and convert it to data type 'int'
    @classmethod
    def decorate_user_input(self, uInput):
        self.uInput = uInput
        regString = re.findall(r'\d+', uInput)
        regList = map(int, regString)
        return regList
    # calculate the average by adding the list elements and return a key for creating dictionary
    def calculate_average(self):
        if self.numList:
            average = sum(self.numList) / len(self.numList)      #two useful built-in methods 'sum' and 'len'
            if average <= 6:
                return 'Low'
            elif 6 < average < 12:
                return 'Medium'
            return 'High'
        return 'Empty'
    # to save the result and display, create a dictionary and assign to specific condition based on key<-> value
    def display_message(self, dKey = ''):
        dict = {'Low': 'Low Average', 'Medium': 'Medium Average', 'High': 'High Average', 'Empty': 'No list found'}
        print dict[dKey]

#pass the list when initializing the class object to get different results
user_input = AverageCalculator.process_user_input()
user_list = AverageCalculator.decorate_user_input(user_input)
aveCal = AverageCalculator(user_list)          # retrieve the result from the created dictionary
aveCal.display_message(aveCal.calculate_average())
