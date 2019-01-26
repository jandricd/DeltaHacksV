import xml.etree.ElementTree as ET
import time

weight = 3500
start = (-94.420307, 44.968046)
end = (-91.493768, 44.240304)

def parseXML(s):

    tree = ET.parse(s)
    root = tree.getroot()

    dataSet = []

    for sample in root:

        samplePoint = { 
        'long' : 0,
        'lat' : 0,
        'weight' : 0,
        'speed' : 0
        }
        
        for field in sample:
            samplePoint[field.tag] = float(field.text)

        dataSet.append(samplePoint)

    return dataSet

def sendInfo(dataSet):

    counter = 0

    for i in range(len(dataSet)):
        print(dataSet[i])
        counter = checkWeight(dataSet[i], counter)
        time.sleep(1)

def alert():
    print("Weight loss detected")

def checkWeight(dataSetDict, counter):
    
    if ((dataSetDict['weight'] < weight) and (counter != 1)):
        alert()
        counter += 1

    return counter

sendInfo(parseXML("GPS_DATA.xml"))

