'''Development of Web Applications and Web Services
    Assignment 1- Python, Exercise 3

    Articles in an application are stored in a folder structure comprised of name, year, month, day added.
    Returns the article name, a representation of the date and how long ago it was stored in days.
    should return something like:  ('my_summer', '21-10-2010', 817)

'''

__author__ = "Dawit Nida (dawit.nida@abo.fi)"
__date__ = "Date: 12.9.2014"
__version__ = "Version: "

import sys
import datetime
import re

class Articles():
    def __int__(self):
        self.article = article
    def process_article(self, article):
        def article_detail():
            articleDate = datetime.date(int(article[1]),int(article[2]),int(article[3]))        # indexing the list and casting to int.  articleDate <type 'datetime.date'>
            # calculate the date difference using delta,
            # check if the result is not zero or less, return the difference
            def date_difference():
                todayDate = datetime.date.today()
                delta = todayDate - articleDate
                if delta.days > 0:
                    return delta.days
                return "Invalid Date"
            # format the date, but no need to change the values while formatting or returning,
            # so tuple is the best, Immutable type
            def format_date():
                dformat = "%d-%m-%Y"
                formattedDate = articleDate.strftime(dformat)
                return formattedDate
            art_tuple = (article[4], format_date(), date_difference())
            # interestingly Python function return Obj and can be used in another function
            return art_tuple
        return article_detail()
    def choose_article(self):
        articleStore = {                                     # store the article in a dictionary with folder structure for manipulation
            'art_0':'articles/2014/09/14/Python_for_computing',
            'art_1':'articles/2008/08/24/Mastering_Github',
            'art_2':'articles/2014/09/15/Web_services',
            'art_3':'articles/2013/04/30/Cloud_computing',
            'art_4':'articles/2013/05/30/Software_as_a_service' }
        print articleStore.keys()
        self.aKey =  raw_input("Choose article ...")        # let the user of this program choose the article
        if self.aKey in articleStore:                      # check if the entered article key exists
            article = re.split("\/+", articleStore[self.aKey])    # use reg expression to separate the article name, date and how old is the article
            return article
        else:
            print 'No such article found!'
            sys.exit()
art = Articles()
article = art.choose_article()
print art.process_article(article)


