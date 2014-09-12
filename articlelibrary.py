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
# from datetime import date
import re

class Articles():
    def __int__(self):
        pass
    # FIXME: Seems like this is working !not check the return
    def process_article(self, article):
        self.article = article
        def article_detail():
            self.article = re.split("\/+", articleStore['art_2'])
            def time_diff():
                articleDate = datetime.date(int(article1[1]),int(article1[2]),int(article1[3]))
                todayDate = datetime.date.today()
                delta = todayDate - articleDate
                return delta.days
            art_tuple = (article1[4], article1[1],article1[2],article1[3], time_diff())
            return art_tuple
        return article_detail()
# TODO: Clean up and loop over the articles
    def traverse(self, articles):
        for k in articles:
            print articles[k]
articleStore = {
    'art_0':'articles/2007/06/18/Python_for_computing',
    'art_1':'articles/2008/08/24/Mastering_Github',
    'art_2':'articles/2012/12/15/Web_services',
    'art_3':'articles/2013/04/30/Cloud_computing',
    'art_4':'articles/2013/04/30/Software_as_a_service'
}


art = Articles()
# art.traverse(articleStore)
article1 = re.split("\/+", articleStore['art_4'])

print art.process_article(article1)





'''

date_formatted = "%Y-%m-%d"
d1 = datetime.date(int(article1[1]),int(article1[2]),int(article1[3]))
d0 = datetime.date.today()

print type(d0), d0
print type(d1), d1

delta = d0 - d1
print delta.days
'''