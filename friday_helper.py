"""Development of Web Applications and Web Services

"""

__author__ = ""
__date__ = "Date: 19.9.2014"
__version__ = "Version: "

import socket

PORT = 8080
HOST = "127.0.0.1"


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

def parse_post_data(inputfile):
    global connection
    connection.shutdown(socket.SHUT_RD)
    '''
    Shutdowns the read direction of the connection, so that we can read the inputfile
    until the EOF marker in order to retrieve the post data
    '''
    for line in inputfile:
        if len(line.strip().replace('\r', '').replace("\n","")) == 0:    #Found the empty line in the request headers
            break
    data_line = inputfile.readline()
    return data_line

def parse_request(request, inputfile):
    lines = request
    if len(lines) < 1:
        return None
    words = lines.split()
    if len(words) < 3:
        return None
    if words[0] == "GET" or words[0] == "POST" and words[2] in ["HTTP/1.0","HTTP/1.1"]:
        method = words[0]
        url = words[1]
        print "Words",words
        if words[0]=="POST":
            post_data = parse_post_data(inputfile)
            return (method, url, post_data)
        else:
            return (method, url, [])
    else:
        return None
