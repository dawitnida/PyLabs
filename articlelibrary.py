'''Development of Web Applications and Web Services
    Assignment 1- Python, Exercise 3

    Articles in an application are stored in a folder structure comprised of name, year, month, day added. E.g. articles/2010/10/21/my_summer
    Write a method that returns the article name, a representation of the date and how long ago it was stored in days.
    (HINT you can perform binary operation on datetime objects like plus and minus, but the operation would return timedelta object)
    E.g. foo("articles/2010/10/21/my_summer")
    should return something like:
    ('my_summer', '21-10-2010', 817)

'''

__author__ = "Dawit Nida (dawit.nida@abo.fi)"
__date__ = "Date: 12.9.2014"
__version__ = "Version: "

import datetime
from datetime import timedelta
import re

class Articles():
    def __int__(self):
        pass
    def process_article(self, article):
        self.article = article
        # FIXME
        print article
        def article_detail():
            #self.article = re.split("\/+", articleStore['art_2'])
            articleDate = datetime.date(int(article[1]),int(article[2]),int(article[3]))
            def date_difference():
                todayDate = datetime.date.today()
                delta = todayDate - articleDate
                if delta.days > 0:
                    return delta.days
                return "Invalid Date"
            def format_date():
                dformat = "%d-%m-%Y"
                formattedDate = articleDate.strftime(dformat)
                return formattedDate
            art_tuple = (article[4], format_date(), date_difference())  #
            return art_tuple
        return article_detail()
    def chose_article(self):
        articleStore = {
            'art_0':'articles/2014/09/14/Python_for_computing',
            'art_1':'articles/2008/08/24/Mastering_Github',
            'art_2':'articles/2012/12/15/Web_services',
            'art_3':'articles/2013/04/30/Cloud_computing',
            'art_4':'articles/2013/05/30/Software_as_a_service' }
        print articleStore.keys()
        self.aKey =  raw_input("Enter article ...")
        if self.aKey in articleStore:
            article = re.split("\/+", articleStore[self.aKey])
            return article
        else:
            print 'No article found!'
            # FIXME
            print articleStore.keys()
            self.chose_article()
art = Articles()
article = art.chose_article()
print art.process_article(article)


