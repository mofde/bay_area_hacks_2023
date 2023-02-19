import maskpass
usernameInput = input("Username: ")
passwordInput = maskpass.askpass(prompt = "Password: ", mask = "*")
