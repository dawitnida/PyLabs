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
import socket
import re
import time
import os

PORT = 8080
HOST = "127.0.0.1"


VALID = 1
WRONG_PASSWD = 2
INVALID_DATE = 3
INVALID_INPUT = 4


def read_request(content):
    return content.readline()

def getHeader(connection):
    current_chunk = connection.recv(1)
    recieved_msg = current_chunk
    while current_chunk != '':
        current_chunk = connection.recv(1)
        recieved_msg = recieved_msg + current_chunk
        if "\r\n\r\n" in recieved_msg:
            break
    return recieved_msg

def getContentLenght(header):
    lines = header.split("\r\n")
    for line in lines:
        if "Content-Length:" in line:
            s = line.split(":")
            return int(s[1])
    return 0

def getBody(connection, contentLenght):
    return connection.recv(contentLenght)


def parse_request(request, connection):
    lines = request

    if len(lines) < 1:
        return None
    words = lines.split()

    if len(words) < 3:
        return None
    if words[0] == "GET" or words[0] == "POST" and words[2] in ["HTTP/1.0", "HTTP/1.1"]:
        method = words[0]
        url = words[1]
        if words[0] == "POST":
            content_lenght = getContentLenght(request)
            if content_lenght != 0:
                data_line = getBody(connection, content_lenght)
                return (method, url, data_line)
        else:
            return (method, url, [])
    else:
        return None


def server(handler, port=PORT, host=HOST, queue_size=5):

    dewas_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dewas_socket.bind((host, port))
    dewas_socket.listen(queue_size)

    while True:
        print "Waiting at http://%s:%d" % (host, port)
        (connection, addr) = dewas_socket.accept()
        print "New connection", connection, addr
        handler(connection)
        connection.close()
        print "Connection closed."

# check if the user input is valid and password is correct
# if so proceed to show if it's Friday otherwise return state
def parse_post_data(data_line):
    if data_line:
        date = re.findall(r'\d{8}', data_line)
        passwd = re.findall(r"&passwd=?(.*)", data_line)
        if date and date[0] and passwd[0]:
            acp_date = validate_date_url(date[0])
            if acp_date:
                if passwd[0] == "friday":
                    return (VALID, acp_date)
                else:
                    save_log(passwd[0])
                    return (WRONG_PASSWD, '')
            return (INVALID_DATE, '')
    return (INVALID_INPUT, '')


def sendResponse(response, connection):
    connection.sendall(response)

def create_document(s):
    return "Content-Type: text/html;\n\r\n\r" + \
           "<html><body>\n\r" + s + "</body></html>\n\r"

def create_response(status, s):
    return "HTTP/1.1 " + status + "\n\r" + \
           s + "\n\r"

# form
def send_form_document(s):
    return "Content-Type: text/html;\n\r\n\r" + \
           "<html><body>" + \
           "<form method ='POST' action =''" + "target = '_self'>" + \
           "Date Text: <input type='text' name='dateText' value=''><br>" + \
           "Password:  <input type='password' name='passwd'><br>" + \
           "<input type='submit' value='submit'> </form>\n\r" + \
           s + "</body></html>"

def remove_slash(params):
    try:
        input_url = re.sub("^/", "", params)
        return input_url
    except IndexError:
        return None

# check if the inserted date on the url exists and return datetime Obj.
def validate_date_url(url):
    if (len(url) == 8) & (url.isdigit()):
        try:             # validate the date exist in calendar
            time.strptime(url, '%d%m%Y')
            dmy = datetime.date(int(url[4:8]), int(url[2:4]), int(url[0:2]))    #convert the string to datetime Obj
            return dmy
        except ValueError:
            return None
    else:
        return None

# read log file
def read_log():
    if os.path.isfile("./log.txt"):
        with open("log.txt", "r") as logfile:
            logfile = logfile.read().strip('\n')
        return logfile
    else:
        return "No log found"

# save log to text file
def save_log(wrong_pass):
    logtime = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
    with open("log.txt", "a") as logfile:
        logfile.write(logtime + " user entered incorrect password: " + wrong_pass + "\n")
    logfile.close()


def is_it_friday(d):
    if d.isoweekday() == 5:
        return "Yes, it is Friday!"
    else:
        return "Nope."

def friday_web_app(connection):
    response = ""
    header = getHeader(connection)
    parameters = parse_request(header, connection)
    input_url = remove_slash(parameters[1])
    input_date_url = validate_date_url(input_url)
    if input_url:
        if input_date_url:
            input_date_url = validate_date_url(input_url)
            response = create_response(
                "200 OK",
                create_document(is_it_friday(input_date_url))
            )
        elif input_url == 'log':
            response = create_response(
                "200 OK",
                create_document(read_log())
            )
        elif input_url == 'dateform':
            post_data = parse_post_data(parameters[2])
            if post_data[0] == 1:
                response = create_response(
                    "200 OK",
                    create_document(is_it_friday(post_data[1]))
                )
            if post_data[0] == 2:
                response = create_response(
                    "200 OK",
                    send_form_document("Wrong password, was it 'friday'?")
                )
            if post_data[0] == 3:
                response = create_response(
                    "200 OK",
                    send_form_document("Check your date, eg. 12121900")
                )
            if post_data[0] == 4:
                response = create_response(
                    "200 OK",
                    send_form_document("Enter date[eg. 12122014] and password ='friday'")
                )
        else:
            response = create_response(
                "400 Bad Request",
                create_document("Precondition Failed!")
            )

    else:
        response = create_response(
            "400 Bad Request",
            create_document("Bad Request!")
        )

    sendResponse(response, connection)

server(friday_web_app)


