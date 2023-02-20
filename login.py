import maskpass
import csv
from csv import writer

startQuestions = False

def login() -> int:
    login = 0
    while login == 0:
        usernameInput = input("Username: ")
        passwordInput = maskpass.askpass(prompt = "Password: ", mask = "*")
        with open("usernames_and_passwords.csv", 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if usernameInput == row["Username"] and passwordInput == row["Password"]:
                    return 1
            print("Username or password is incorrect")

def createNewAccount() -> int:
    newAccountCreated = 0
    while newAccountCreated == 0:
        usernameInput = input("Username: ")
        passwordInput = maskpass.askpass(prompt = "Password: ", mask = "*")
        confirmPasswordInput = maskpass.askpass(prompt = "Confirm Password: ", mask = "*")
        if passwordInput == confirmPasswordInput:
            newAccountCreated = 1
    with open("usernames_and_passwords.csv", 'a', newline = '') as csv_file:
        writer_object = writer(csv_file)
        writer_object.writerow([usernameInput, passwordInput])
        csv_file.close()
    return 1