from __init__ import *

if __name__ == "__main__":
    accountInput = input("Do you currently have an account? ")
    if accountInput.lower() == "yes":
        login()
    else:
        createNewAccount()