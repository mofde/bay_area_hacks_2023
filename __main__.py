import maskpass
import csv
from csv import writer

from login import startQuestions, login, createNewAccount
from intro_ques import introvert, extrovert, ask, prompt, findDescription, findHobby, findLandscape, findMovie
from save_objects import saveObj, readObj
import subprocess
import socket

loggedIn = False

if __name__ == "__main__":
    accountInput = input("Do you currently have an account? ")
    if accountInput.lower() == "yes":
        usernameInput = login()
        loggedIn = True
    else:
        usernameInput = createNewAccount()
        loggedIn = True

if loggedIn == True:
    if ask() == "i":
        newPerson = introvert(usernameInput)
    elif ask() == "e":
        newPerson = extrovert(usernameInput)
    saveObj(newPerson.type, newPerson._description, newPerson._hobby, newPerson._landscape, newPerson._movie)

if loggedIn == True:
    subprocess.run(['python', 'server.py'])

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

