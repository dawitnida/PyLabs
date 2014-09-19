"""Development of Web Applications and Web Services

"""

__author__ = "Dawit Nida (dawit.nida@abo.fi)"
__date__ = "Date: 19.9.2014"
__version__ = "Version: "

import socket
import datetime
from friday_helper import read_request, parse_request

PORT = 8080
HOST = "127.0.0.1"


def parse_post_data(inputfile):
    global connection
    connection.shutdown(socket.SHUT_RD)
    '''
    Shutdowns the read direction of the connection, so that we can read the inputfile
    until the EOF marker in order to retrieve the post data
    '''
    for line in inputfile:
        if len(line.strip().replace('\r', '').replace("\n", "")) == 0:     # Found the empty line in the request headers
            break
    data_line = inputfile.readline()
    return data_line


def server(handler, port=PORT, host=HOST, queue_size=5):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.bind((host, port))
    mysocket.listen(queue_size)
    while True:
        print "Waiting at http://%s:%d" % (host ,port)
        (connection,addr) = mysocket.accept()
        print "New connection",connection,addr
        inputfile = connection.makefile('rb' ,-1)
        outputfile = connection.makefile('wb' ,0)
        handler(inputfile ,outputfile)
        inputfile.close()
        outputfile.close()
        connection.close()
        print "Connection closed."

def create_document(s):
    return "Content-Type: text/html;\n\r\n\r" + \
           "<html><body>\n\r"+s+"</body></html>\n\r"

def create_response(status ,s):
    return "HTTP/1.1 "+status+"\n\r" + \
           s+"\n\r"

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
import re
import time
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


def is_it_friday(d):
    if d.isoweekday() == 5:
        return "Yes, it is Friday!"
    else:
        return "Nope."

server(friday_webapp)

