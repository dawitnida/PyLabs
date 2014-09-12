PythonAssignment-1
==================

1. Define a class in Python that has an average function which calculates the average value of the numbers from a list. You can pass the list when you initialize the class
object. If the average is less than 6, print “Low Average”, if average is between 6 and 12 print “Medium Average” and if average is greater than 12 print “High Average”.
The output messages MUST be save in a dictionary with keys, e.g. a, b ,c for different conditions mentioned above. The output messages must be retrieved from this
dictionary when printing.
2. Update the program in Example 1, such that it should be able to take a string of mixed letters and numbers from the user, parse out numbers from it and initialize the
class object.
(HINT use re.findall with a regular expression to extract numbers from a string and you can add a new method in the class with @classmethod decorator. This method
could extract a list of numbers and initialize the object.)
E.g. with the string "l33t h4x0r 1s pwn3d"
The method should extract this [33,4,0,1,3] from the string to initialize the object.
3. Articles in an application are stored in a folder structure comprised of name, year, month, day added. E.g. articles/2010/10/21/my_summer
Write a method that returns the article name, a representation of the date and how long ago it was stored in days.
(HINT you can perform binary operation on datetime objects like plus and minus, but the operation would return timedelta object)
E.g. foo("articles/2010/10/21/my_summer")
should return something like:
('my_summer', '21-10-2010', 817)
