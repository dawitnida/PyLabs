"""Development of Web Applications and Web Services
    # TASK 1
    A user can send any date to the server using the following url pattern:
    http://127.0.0.1:8080/ddmmyyyy and in response the server
    notify the user whether it is Friday on the given date or not.

    # TASK 2
    A user is able to fetch a date form from the server by entering:
    http://127.0.0.1:8080/dateform
        The form have:
        a) Text field
        b) Password field
        c) Submit button
    A user can enter a date in the Text field and a password.

    # TASK 3
    A user is able to fetch the content of the log file by entering:
    http://127.0.0.1:8080/log
"""

__author__ = "Dawit Nida (dawit.nida@abo.fi)"
__date__ = "Date: 19.9.2014"
__version__ = "Version: "

import datetime
import re
import time

from friday_helper import server, parse_request, parse_post_data

def read_request(inputfile):
    return inputfile.readline()

def create_document(s):
    return "Content-Type: text/html;\n\r\n\r" + \
           "<html><body>\n\r"+s+"</body></html>\n\r"

def create_response(status ,s):
    return "HTTP/1.1 "+status+"\n\r" + \
           s+"\n\r"

#TASK 2: Form
def send_form_document():
    return "Content-Type: text/html;\n\r\n\r" + \
           "<html><body>"+\
           "<form action=" +  "method ='POST'>" + \
           "Date Text: <input type='text' name='dateText'> <br/>" + \
           "Password: <input type='password' name='passwd'> <br/>" + \
           "<input type='submit'> </form>" + "</body></html>"

def friday_webapp(inputfile, outputfile):
    request = read_request(inputfile)
    if parse_request(request, inputfile):
        url = parse_request(request, inputfile)[1]

        if validate_date_url(url):
            date_url = validate_date_url(url)
            response = create_response(
                "200 OK",
                create_document(is_it_friday(date_url))
                )
        elif validate_dateform_url(url):
            print "Url", parse_request(request, inputfile)[1]
            response = create_response(
                    "200 OK",
                    send_form_document()
                    )
        elif validate_log_url(url):
            print "Log", validate_log_url(url)
            response = create_response(
                    "200 OK",
                    create_document("File logger")
                    )
        else:
           response = create_response(
            "412 Precondition Failed",
            create_document("Precondition Failed!")
            )
    else:
        response = create_response(
            "400 Bad Request",
            create_document("Bad Request pal!")
            )
    send_response(outputfile, response)

def send_response(outputfile, s):
    outputfile.write(s)

#TASK 1
def validate_date_url(url):
    url = re.sub("^/","", url)
    if len(url) == 8:
        try:             # validate the date exist in calendar
            time.strptime(url, '%d%m%Y')
            dmy = datetime.date(int(url[4:8]), int(url[2:4]), int(url[0:2]))    #convert the string to datetime Obj
            return dmy
        except ValueError:
            return None
    else:
        return None

#TASK 2
def validate_dateform_url(url):
    url = re.sub("^/","", url)
    if url == 'dateform':
        return True
    return None

def process_post_data():
    return 'String'

#TASK 3
def validate_log_url(url):
    url = re.sub("^/","", url)
    if url == 'log':
        return True
    return None


def is_it_friday(d):
    if d.isoweekday() == 5:
        return "Yes, it is Friday!"
    else:
        return "Nope."


server(friday_webapp)

