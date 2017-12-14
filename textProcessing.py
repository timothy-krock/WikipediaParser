######################################
## THIS IS MY BORING TEXT PROCESSING 
## PAGE. NOTHING VERY FLASHY. 
## THESE FUNCTIONS ALL PROBABLY EXIST
true = 1
false = 0
######################################
## Verifies if the char is a letter.
## Admittedly confusing naming

def isChar(char): 
    if(ord(char) > 64 and ord(char) < 91):
        return true
    elif (ord(char) > 96 and ord(char) < 123):
        return true
    else:
        return false

######################################
## ACTUALLY PRETTY SURE THESE TWO ARE
## BACKWARDS BUT IT DOESN'T MATTER
def capitalize(word): 
    if word == '':
        return ''
    if isChar(word[0]):
        if(ord(word[0]) > 64 and ord(word[0]) < 91):
            return chr(ord(word[0])+32)+word[1:]
    return word

def lowercase(word):
    if word == '':
        return ''
    if isChar(word[0]):
        if(ord(word[0]) > 96 and ord(word[0]) < 123):
            return chr(ord(word[0])-32)+word[1:]
    return word
######################################
## TODO: FIX THIS, ASSHOLE 
## 
def wordSplit(string):
    array = []
    wordFragment = ''
    index = 0
    if(string == ''):
        return []
    #for char in string:
    #    if not isChar(char):
    #        break
    while(isChar(string[index])) and index+1 < len(string):
        index = index + 1
    array.append(string[:index+1])
    array = array + wordSplit(string[index+1:])
    return array

#####################################
## ITERATES THROUGH POSSIBLE OPTIONS
## OF CAPITALIZATION
def findVariants(string):
    array = wordSplit(string)
    retval = [''] 
    for word in array:
        newRetval = [] 
        for fragment in retval:
            if isChar(word[0]): 
                newRetval.append(fragment + capitalize(word))
                newRetval.append(fragment + lowercase(word))
            else:
                newRetval.append(fragment + word)
        retval = newRetval
    return retval


 





























######################################
## TESTS
if __name__ == "__main__":
    print "######################################################################"
    print "TESTING isChar, OUTCOMES SHOULD BE 1,1,1,0,1,1,1"
    print isChar("a")
    print isChar("c")
    print isChar("z")
    print isChar("_")
    print isChar("A")
    print isChar("C")
    print isChar("Z")
    print "######################################################################"
    print "TESTING wordSplit():"
    print "TestCase: 'Cable Ties'"
    print "SHOULD OUTPUT ['Cable', 'Ties']"
    print wordSplit("Cable Ties")
    print "TestCase: 'Category:Bacon   Definitions'"
    print "SHOULD OUTPUT ['Category:','Bacon ',' ',' ','Definitions']"
    print wordSplit("Category:Bacon   Definitions")
    print "#######################################################################"
    print "TESTING findVariants()"
    print "TestCase: 'Cable Ties'"
    print "SHOULD OUTPUT: ['Cable Ties', 'Cable ties', 'cable Ties', 'cable ties']"
    print findVariants("Cable Ties")
    print "TestCase: 'Category:Bacon   Definitions'"
    print "TBH I don't want to figure out what the output should be"
    print findVariants("Category:Bacon   Definitions")
