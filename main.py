from __init__ import *
import socket

loggedIn = False

if __name__ == "__main__":
    accountInput = input("Do you currently have an account? ")
    if accountInput.lower() == "yes":
        if login() == 1:
            loggedIn == True
    else:
        if createNewAccount() == 1:
            loggedIn == True

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







