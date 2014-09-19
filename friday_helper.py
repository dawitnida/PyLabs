"""Development of Web Applications and Web Services

"""

__author__ = ""
__date__ = "Date: 19.9.2014"
__version__ = "Version: "

import socket
def read_request(inputfile):
    return inputfile.readline()

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
    lines=request
    print "Lines in parse_request{}", lines    #FIXME
    if len(lines)<1:
        return None
    words = lines.split()
    print "Words in parse_request{}", words, len(words) #FIXME
    if len(words)<3:
        return None
    if words[0]=="GET" or words[0]=="POST" and words[2] in ["HTTP/1.0","HTTP/1.1"]:
        method = words[0]
        url = words[1]
        print "Method" + method + "url" + url + "word 2" + words[2]    #FIXME

        if words[0]=="POST":            #FIXME
            post_data = parse_post_data(inputfile)
            # return (method, url, post_data)
            return True
        else:                  #FIXME
            return (method, url, [])
    else:                  #FIXME
        return False # None
