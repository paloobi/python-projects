import os

def changeSlashes(fileList):
# given a list of files, returns a new list
# converts double \\ to / for use in web URLs
        newFileList = []
        for name in fileList:
                newName = ""
                for letter in name:
                        if letter == "\\":
                                newName += "/"
                        else:
                                newName += letter
                newFileList.append(newName)
        return newFileList

def createFileList():
# creates a list of all files, recursively, in a directory
        fileList = []
        for item in os.walk(".", followlinks=True):
                for name in item[-1]:
                        if name[-3:] == "htm" or name[-4:] == "html":
                                fileList.append(item[0][2:] + "/" + name)
        fileList = changeSlashes(fileList)
        return fileList

def createTopicMapping(fileName):
# Creates a file that maps each help file path to an empty string
# fileName - string, the name and extension for the output file
        fileList = createFileList()
        topicFile = open(fileName, "w")
        for item in fileList:
                topicFile.write('if (P === "") C = "' + item + '";\n')
        topicFile.close()

createTopicMapping("topics-4.txt")
