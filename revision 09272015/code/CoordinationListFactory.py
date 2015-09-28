'''
Created on 2015/9/25

@author: ChengYuan
'''
import os
def generateCoordinationList(filePath):
    coordinationList = []
    absGraphFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__), filePath));
    with open(absGraphFilePath, "r") as f:
        for line in f:
            if line.strip()[0] != "#":
                coordinate = line.split(" ")
                coordinationList.append((int(coordinate[1]), int(coordinate[2])))
    return coordinationList