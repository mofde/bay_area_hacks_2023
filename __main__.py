import maskpass
import csv
from csv import writer

from login import startQuestions, login, createNewAccount
from intro_ques import introvert, extrovert, ask, prompt, findDescription, findHobby, findLandscape, findMovie
from save_objects import saveObj, readObj
import socket

loggedIn = False

if __name__ == "__main__":
    accountInput = input("Do you currently have an account? ")
    if accountInput.lower() == "yes":
        if login() == 1:
            loggedIn = True
    else:
        if createNewAccount() == 1:
            loggedIn = True

if loggedIn == True:
    if ask() == "i":
        newPerson = introvert()
    elif ask() == "e":
        newPerson = extrovert()
    saveObj(newPerson)
saveList = []
choiceList = ["introvert", "extrovert"]
saveList.append(newPerson.username)
saveList.append(newPerson.type)
saveList.append(newPerson._description)
saveList.append(newPerson._hobby)
saveList.append(newPerson._landscape)
saveList.append(newPerson._movie)
choiceList.remove(newPerson.type)
strChoiceList = str(choiceList)
friendUser = readObj(saveList, strChoiceList)

