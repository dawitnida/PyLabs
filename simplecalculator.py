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
         #  return dict['Low']
        elif resultKey == 'Medium':
            dict["Medium"] = "Medium Average"
         #  print  dict['Medium']
        elif resultKey == 'High':
            dict["High"] = "High Average"
         #  print  dict['High']
        else:
            dict['Empty'] = "List is empty"
         #  print  dict['Empty']
        return dict

# lists of list for case study => output depends on the list
list1 = [11,0,0,9]
list2 = [6,8]
list3 = [10,12,14,21]
list4 = []

#pass the list when initializing the class object.
defCal = AverageCalculator(list1)
# retrieve the result from the created dictionary
display_list1 = defCal.create_dict(defCal.calculate_average())
print  display_list1.values()
''' Display different results
defCal = AverageCalculator(list2)
display_list1 = defCal.create_dict(defCal.calculate_average())
defCal = AverageCalculator(list3)
display_list1 = defCal.create_dict(defCal.calculate_average())
defCal = AverageCalculator(list4)
display_list1 = defCal.create_dict(defCal.calculate_average())
'''



