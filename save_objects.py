import csv
from csv import writer

def saveObj(description = "", hobby = "", landscape = "", movie = ""):
    people = open("people.csv", "w")
    username = input("enter your username: ")
    writer_object = writer(people)
    writer_object.writerow([username, description, hobby, landscape, movie])
    people.close()

def readObj(description):
    people = open("people.csv", "r")
    compareList = []
    returnList = []
    c = 0
    cC = 1
    returnDict = {}
    csv_reader = csv.DictReader(people)
    for i in csv_reader:
        if c <= 5:
            compareList.append(i)
            c += 1
        if c >= 5:
            for name in compareList:
                if description == name:
                    returnDict[cC] = name
                cC += 1
                if cC >= 5:
                    cC = 0
            c = 0
            if len(returnDict) >= 2:
                returnList = [1, compareList[0]]
                return returnList
            else:
                returnList = [0, compareList[0]]
                return returnList

    people.close()


