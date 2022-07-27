
def populateTxtFile(myString,textFileString):
    myfile = open(textFileString,'w')
    myfile.write(myString)
    myfile.close

def pruneStringWith(myString, fileName = "links.txt"):
    bigList = []
    myList = []
    myWFile = open(fileName,"r")
    for line in myWFile:
        if line == "\n":
            bigList.append(myList)
            myList = []
        else:
            myList.append(line)
    myWFile.close
    myRFile = open("prunedwith.txt", "w")
    for list in bigList:
        if myString in list[0]:
            for item in list:
                myRFile.write(item)
            myRFile.write('\n')
    myRFile.close

def pruneString(myString, fileName = "links.txt"):
    bigList = []
    myList = []
    myWFile = open(fileName,"r")
    for line in myWFile:
        if line == "\n":
            bigList.append(myList)
            myList = []
        else:
            myList.append(line)
    myWFile.close
    myRFile = open("prunedwithout.txt", "w")
    for list in bigList:
        if myString not in list[0]:
            for item in list:
                myRFile.write(item)
            myRFile.write('\n')
    myRFile.close