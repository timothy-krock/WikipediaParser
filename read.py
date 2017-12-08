import bz2
import json
import xml.etree.ElementTree as ET

#####################################################
## NOTE: There are 17,807,119 pages in this dump.




def searchHash(word):
    print "OPENING FILE" 
    file = open("small.json")
    print "PARSING AS JSON"
    data = json.load(file)
    file.close()
    print "SEARCHING"
    print data["Anarchism"]
######################################################
## SEARCH INDEX FOR word, OR CLOSEST MATCH
## RETURN [{
##          offset: NUM, (PAGE OFFSET)
##          end: NUM, (END OF PAGE)
##          title: TITLE, 
##          index: INDEX, (INDEX OF PAGE IN XML PAGE
##        },...(POSSIBLY MULTIPLE)]
def search(word):
    file = open('enwiki-20170901-pages-articles-multistream-index.txt', 'rb')
    i = 0
    j = 0
    array = []
    offsets = {}
    hashingJSON = {}
    previous = '616'
    while(i < 17807120):
        colonIndex1 = 0
        colonIndex2 = 0
        str = file.readline()
        
        for charIndex in range(len(str)):
            #if(str[charIndex] == ":"):
            #    offsets[int(str[:charIndex])] = 1
            #    break
            if(str[charIndex] == ":"):
                if not colonIndex1:
                    colonIndex1 = charIndex
                else: 
                    colonIndex2 = charIndex
                    break
        hashingJSON[str[colonIndex2+1:-1]] = i
        if str[:colonIndex1] != previous:
            j = j + 1
            array.append(previous)
            print previous
            previous = str[:colonIndex1]
        i = i + 1   

        





    file.close
    #print hashingJSON
    stringJSON = json.dumps(array)
    #print offsets
    file2 = open("cutoffs.json","w")
    file2.write(stringJSON)
    file2.close()

#######################################################
## RETURNS AN XML CHUNK PAGED IN FROM THE BZ2 FILE

def lookup(offset, end):
    file = open('enwiki-20170901-pages-articles-multistream.xml.bz2', 'rb')
    file.seek(offset)

    chunk = file.read(end-offset)

    xml = bz2.decompress(chunk)
    xml = "<rootNode>" + xml + "</rootNode>"
    return  ET.fromstring(xml)
    file.close()
########################################################
##  RETURNS THE TEXT OF AN ARTICLE IN THE GIVEN  XML 
##  ROOT AT THE GIVEN INDEX IN THE XML FILE
def getPage(root, idx):
     
    for child in root[idx]:
        print child.tag
        for attrib in child:
            print child.tag, " : ",  attrib.tag
            #print "  VALUE:   ", attrib.text
    return root[idx]
    #print root[idx][3][8].text 
    
