############################################
## SERVER CODE HANDLES SEARCH FOR 
## INDIVIDUAL ARTICLES
## 
## THIS NEEDS TO EXIST BECAUSE PARSING OUR 
## LARGE JSONS IS VERY SLOW. IF WE'RE GOING
## TO DO SO MULTIPLE TIMES, THEN WE SHOULD
## KEEP IT PARSED. ERGO, SERVER. 
#!/usr/bin/env python
import signal
import sys
import socket
import time
import json
SERVER_STARTED = 0


#########################################
## SIGNAL HANDLER CODE
def signalHandler(signal, frame):
        print('You pressed Ctrl+C!')
        if SERVER_STARTED:
            serversocket.close()
        sys.exit(0)
signal.signal(signal.SIGINT, signalHandler)



###########################################
## HELPER FUNCTION STARTS SERVER
def startServer():
    print "STARTING SERVER"
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 8089))
    serversocket.listen(5) # become a server socket, maximum 5 connections
    SERVER_STARTED = 1
    return serversocket

##########################################
## HELPER FUNCTION LOADS JSON
def loadJSON():
    print "OPENING FILE"
    file = open("small.json")
    print "PARSING AS JSON"
    data = json.load(file)
    print "JSON LOADED"
    file.close()
    return data


if __name__ == "__main__":
    serversocket = startServer()
    data = loadJSON()


    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(64)
        if len(buf) > 0:
            print buf
            try:
                value = data[buf]
            except:
                print "VALUE NOT FOUND" 
                value = "VALUE NOT FOUND" 
            connection.send(str(value))
