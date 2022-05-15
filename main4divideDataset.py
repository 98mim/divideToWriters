from xml.dom import minidom
from os import listdir
import os.path
from os import path
from os.path import isfile, join
import shutil
import os
import pathlib

folder = 'words'
onlyfiles = [f for f in listdir('xml') if isfile(join('xml', f))]


def readXML(name):
    # parse an xml file by name
    file = minidom.parse(name)

    # use getElementsByTagName() to get tag
    models = file.getElementsByTagName('form')

    # one specific item attribute
    print('model #2 attribute:')
    print(models[0].attributes['id'].value)
    print(models[0].attributes['writer-id'].value)
    words = file.getElementsByTagName('word')
    return [models[0].attributes['id'].value, models[0].attributes['writer-id'].value, words]


def moveDir(startDir, destDir):
    # getting all the files in the source directory
    # files = os.listdir(startDir)

    # shutil.copytree(startDir, destDir)
    shutil.move(startDir, destDir)


def checkDir(dirPath):
    dir = pathlib.Path(dirPath)
    if dir.exists():
        print("File exist")
    else:
        print("File not exist")
        os.mkdir(dirPath)


def addTextFile(path_to_file, text):
    f = open(path_to_file, 'w')
    f.write(text)


for file in onlyfiles:
    infos = readXML('xml/' + file)
    checkDir('writers/' + infos[1])
    for i in infos[2]:
        wrId = i.attributes['id'].value
        wrText = i.attributes['text'].value
        print(wrId)
        spl = infos[0].split('-')
        a = len(wrText)
        checkDir('writers/' + infos[1] + '/' + str(len(wrText)))
        addTextFile('writers/' + infos[1] + '/' + str(len(wrText)) + '/' + wrId + '.txt', wrText)
        moveDir(folder + '/' + spl[0] + '/' + infos[0] + '/' + wrId + '.png',
                'writers/' + infos[1] + '/' + str(len(wrText)) + '/' + wrId + '.png')

