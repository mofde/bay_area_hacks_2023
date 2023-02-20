import maskpass
import csv
def login():
    usernameInput = input("Username: ")
    passwordInput = maskpass.askpass(prompt = "Password: ", mask = "*")
    with open("usernames_and_passwords.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if usernameInput == row["Username"] and passwordInput == row["Password"]:
                return
        print("Username or password is incorrect")

if __name__ == "__main__":
    login()