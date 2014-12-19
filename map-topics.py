import os

def createFileList():
# creates a list of all files, recursively, in a directory
        fileList = []
        for item in os.walk(".", followlinks=True):
                for name in item[-1]:
                        if name[-3:] == "htm" or name[-4:] == "html":
                                directory = item[0][2:] + "/" + name
                                directory = directory.replace("\\", "/")
                                fileList.append(directory)
        return fileList

def createTopicMapping(fileName):
# Creates a file that maps each help file path to an empty string
# fileName - string, the name and extension for the output file
        fileList = createFileList()
        topicFile = open(fileName, "w")
        for item in fileList:
                topicFile.write('if (P === "") C = "' + item + '";\n')
        topicFile.close()

fileName = raw_input("Name and extension of the output file: ")

createTopicMapping(fileName)

