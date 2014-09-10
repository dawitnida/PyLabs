""" Development of Web Applications and Web Services 
    Assignment 1- Python

    This program calculates the average number from a List and display result fetched from dictionary object
"""

__author__ = 'Dawit Nida (dawit.nida@abo.fi)'
__date__ = '$Date: 2014-09-05 21:57:19 $'


class AverageCalculator():
    def __init__(self, numList = []):
         self.nList = numList
    # calculate the average by adding the list elements and return a key for creating dictionary
    def calculate_average(self):
        if self.nList:
            average = sum(self.nList) / len(self.nList)      #two useful built-in methods 'sum' and 'len'
            if average <= 6:
                return 'Low'
            elif 6 < average < 12:
                return 'Medium'
            return 'High'
        return 'Empty'
    #to save the result and display, create a dictionary and assign to specific condition based on key<-> value
    def create_dict(self, resultKey = ""):
        self.resultKey = str(resultKey)
        dict = {}
        if resultKey == 'Low':
            dict["Low"] = "Low Average"
        elif resultKey == 'Medium':
            dict["Medium"] = "Medium Average"
        elif resultKey == 'High':
            dict["High"] = "High Average"
        else:
            dict['Empty'] = "List is empty"
        return dict

# lists of list for case study => output depends on the list
list1 = [11,0,0,21]
list2 = [6,8]
list3 = [10,12,14,21]
list4 = []

#pass the list when initializing the class object to get different results
simpleCal = AverageCalculator(list2)
# retrieve the result from the created dictionary
dictionaryResult = simpleCal.create_dict(simpleCal.calculate_average())
print  dictionaryResult.get(simpleCal.calculate_average())      # display the value using 'get' method of dictionary



