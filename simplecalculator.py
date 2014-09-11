''' Development of Web Applications and Web Services
    Assignment 1- Python, Exercise 1

    This program calculates the average number from a List and display result fetched from dictionary object,
    If the average is less than 6, print 'Low Average', if average is between 6 and 12 print 'Medium Average' and
    if average is greater than 12 print 'High Average'.
'''

__author__ = 'Dawit Nida (dawit.nida@abo.fi)'
__date__ = '$Date: 2014-09-05 21:57:19 $'


class AverageCalculator():
    def __init__(self, numList = []):
         self.numList = numList
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
    #to save the result and display, create a dictionary and assign to specific condition based on key<-> value
    def display_message(self, dKey = ''):
        dict = {'Low': 'Low Average', 'Medium': 'Medium Average', 'High': 'High Average', 'Empty': 'No list found'}
        return dict[dKey]

# lists of list for case study => output depends on the list
list0 = [-12]
list1 = [1,0,0,1]
list2 = [6,8]
list3 = [10,12,14,21]
list4 = []

#pass the list when initializing the class object to get different results
simpleCal = AverageCalculator(list0)
# retrieve the result from the created dictionary
dictionaryResult = simpleCal.display_message(simpleCal.calculate_average())
print  dictionaryResult


