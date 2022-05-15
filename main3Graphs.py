import matplotlib.pyplot as plt
from xml.dom import minidom
from os import listdir
import os.path
from os import path
from os.path import isfile, join
import shutil
import os
import pathlib
import numpy as np
import plotly.express as px


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
    wrId = words[0].attributes['id'].value
    wrText = words[0].attributes['text'].value
    return [models[0].attributes['id'].value, models[0].attributes['writer-id'].value, words]


"""writers = {}

for file in onlyfiles:
    infos = readXML('xml/' + file)
    if infos[1] in writers:
        num = writers.get(infos[1])+1
        writers[infos[1]] = num
    else:
        writers[infos[1]] = 1
keys = []
values = []
items = writers.items()
print(writers)
for item in items:
    #if item[1]>5:
    keys.append(item[0]), values.append(item[1])

y = np.array(values)
plt.pie(y, labels = keys)
#plt.legend(title = "Writers id:")
plt.show()
fig = px.pie(values=values, names=keys, title='Writers pages')
fig.show()"""



count = []
lengths = []
for i in range(1, 18):
    dir = 'writers/000/'+str(i)
    onlyfiles = listdir(dir)
    print(onlyfiles.__len__()/2)
    lengths.append(i), count.append(onlyfiles.__len__()/2)

y = np.array(count)
plt.pie(y, labels = lengths)
#plt.legend(title = "Word lengts:")
plt.show()
fig = px.pie(values=count, names=lengths, title='Writer 000 and lenghts of his words')
fig.show()


'''writers = {}

for file in onlyfiles:
    infos = readXML('xml/' + file)
    if infos[1] in writers:
        num = writers.get(infos[1])+infos[2].__len__()
        writers[infos[1]] = num
    else:
        writers[infos[1]] = infos[2].__len__()
keys = []
values = []
items = writers.items()
print(writers)
for item in items:
    if item[1]>500:
        keys.append(item[0]), values.append(item[1])
y = np.array(values)
plt.pie(y, labels = keys)
#plt.legend(title = "Writers id:")
plt.show()
fig = px.pie(values=values, names=keys, title='Writers with more than 500 words')
fig.show()'''