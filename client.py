####################################################
## CLIENT CODE FOR QUERYING WIKIPEDIA
import socket
import json
from read import * 
from nltk.corpus import wordnet

def getSynonyms(word):
    syns = wordnet.synsets(word)
    print set(syns)


def sendWordToServer(word):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 8089))
    clientsocket.send(word)
    buf = clientsocket.recv(64)
    return buf
    clientsocket.close()

def getRaw(index):
    file = open("cutoffs.json")
    array = json.load(file)
    print array[index/100], ',  ', array[index/100 + 1], ',  ' ,str((index)%100)
    page = lookup(int(array[index/100]), int( array[index/100 + 1]))
    xml = getPage(page, (index)%100)
    string = ""
    for child in xml:
        for child2 in child: 
            print "\n\n" + child2.tag + "\n\n"
            print child2.text    
if __name__ == "__main__":
    while(1):
        char = raw_input("\n\n\n Enter word: ")
        returnString = sendWordToServer(char)
        if returnString != "VALUE NOT FOUND":
            string = getRaw(int(returnString))
        else:
            print "VALUE NOT FOUND"
        getSynonyms(char)
