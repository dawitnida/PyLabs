"""Development of Web Applications and Web Services

"""

__author__ = "Dawit Nida (dawit.nida@abo.fi)"
__date__ = "Date: 19.9.2014"
__version__ = "Version: "

from friday_helper import read_request, parse_request
import socket
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
def process_url():
    pass
def create_response(status ,s):
    return "HTTP/1.1 "+status+"\n\r" + \
           s+"\n\r"

def friday_webapp(inputfile,outputfile):
    request = read_request(inputfile)
    print "Request {}", request
    strDate = ""
    if parse_request(request, strDate):
        response=create_response(
            "200 OK",
            create_document(is_it_friday(datetime.date.today()))
            )
    else:
        response=create_response(
            "400 Bad Request",
            create_document("Bad Request pal!")
            )
    send_response(outputfile,response)

def send_response(outputfile,s):
   outputfile.write(s)

import datetime
def is_it_friday(d):
    if d.isoweekday() == 4:
        return "Yes, it is Friday!"
    else:
        return "Nope."

server(friday_webapp)

