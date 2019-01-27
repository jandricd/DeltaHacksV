import xml.etree.ElementTree as ET
import time
import math

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

def alertWeight():
    print("Weight loss detected")

def alertDist():
    print("Driver has left designated area")

def checkWeight(dataSetDict, counter):
    
    if ((dataSetDict['weight'] < weight) and (counter != 1)):
        alertWeight()
        counter += 1

    return counter

def midRad (start, end):
    mid = (((start[0]+end[0])/2), ((start[1]+end[1])/2))
    radius = math.sqrt(pow(mid[0]-start[0], 2) + pow(mid[1]-start[1], 2))
    return (mid, radius)

def checkCircle(rMtuple, currentPos):
    distanceTrucker = math.sqrt(pow(rMtuple[0][0]-currentPos[0], 2) + pow(rMtuple[0][1]-currentPos[1], 2))

    if (distanceTrucker > rMtuple[1]):
        alertDist()

# sendInfo(parseXML("GPS_DATA.xml"))

