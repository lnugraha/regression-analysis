import sys
sys.path.insert(1,'../src')

import linear
import dataload

import numpy as np
import matplotlib.pyplot as plt
import json

def retrieveJSON(filePath, uniqueKey):
    with open(filePath) as fileData:
        entireData = json.load(fileData)
        # Retrieve independent variable x
        xValues = entireData[0]
        xElements = xValues[uniqueKey[0]]
        # Retrieve dependent variable y
        yValues = entireData[1]
        yElements = yValues[uniqueKey[1]]
    return xElements, yElements

def main():
    snowJSON = "../data/snow/snow.json"
    snowArr, yieldArr = retrieveJSON(snowJSON, ["Snow", "Yield"])
    print(snowArr)
    print(yieldArr)

if __name__ == "__main__":
    main()
