import xml.etree.ElementTree as ET
import time

def parseXML(s):

    tree = ET.parse(s)
    root = tree.getroot()

    dataSet = []

    samplePoint = { 
        'long' : 0,
        'lat' : 0,
        'weight' : 0,
        'speed' : 0
    }

    for sample in root:
        
        for field in sample:
            samplePoint[field.tag] = float(field.text)
        
        dataSet.append(samplePoint)
        
        return dataSet

dataSet = parseXML("parseCoordinates.py")

for i in range(len(dataSet)):
    print(dataSet[i])
    