""" Development of Web Applications and Web Services

"""

__author__ = "Dawit Nida (dawit.nida@abo.fi)"
__date__ = "Date: 19.9.2014"
__version__ = "Version: "


import datetime
       # print "Method" + method + "url" + url + "word 2" + words[2]    #FIXME
url = '05062017'
dmy = datetime.date(int(url[4:8]), int(url[2:4]), int(url[0:2]))

def is_it_friday(d):
    if d.isoweekday() == 5:
        return "Yes, it is Friday!"
    else:
        return "Nope."

print is_it_friday(dmy)