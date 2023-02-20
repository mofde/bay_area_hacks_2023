import csv
from csv import writer

def saveObj(type_of_person = "", description = "", hobby = "", landscape = "", movie = ""):
    people = open("people.csv", "w")
    username = input("enter your username: ")
    writer_object = writer(people)
    writer_object.writerow([username, type_of_person, description, hobby, landscape, movie])
    people.close()

def readObj(description, type):
    # when using this, make sure to have a list of all of the descriptions of the person in the call
    people = open("people.csv", "r")
    compareList = []
    returnList = []
    c = 0
    cC = 1
    returnDict = {}
    csv_reader = csv.DictReader(people)
    for i in csv_reader:
        if c <= 6:
            compareList.append(i)
            c += 1
        if c >= 6:
            for name in compareList:
                if name in description:
                    returnDict[cC] = name
                cC += 1
                if cC >= 6:
                    cC = 0
            c = 0
            if len(returnDict) >= 3 and compareList[1] == type:
                #           did it work, username, type of person
                returnList = [1, compareList[0], compareList[1]]
                return returnList
    people.close()


