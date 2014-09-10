""" Development of Web Applications and Web Services 
    Assignment 1- Python

    This program calculates the average number from a List
"""
__author__ = 'Dawit Nida (dawit.nida@abo.fi)'
__date__ = '$Date: 2014-09-05 21:57:19 $'


class AverageCalculator():
    def __init__(self, numList = []):
         self.nList = numList
    def get_average(self, defaultList = []):
        lth = len(defaultList)
        if lth > 0:
            average = sum(defaultList) / lth
            if average < 6:
                return 'Low'
            elif 6 < average <12:
                return 'Medium'
            return 'High'
        return 1
    def create_dict(self, dict = {}):
        self.dict = dict

list1 = [3,5,7,8,9]
defCal = AverageCalculator(list1)
print defCal.get_average()