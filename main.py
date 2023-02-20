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

if readObj(newPerson._description)[0] == 1:
    friendUser = readObj(newPerson._description)[1]


    client_socket = socket.socket()
    port = 12345
    client_socket.connect(('127.0.0.1',port))

    #recieve connection message from server
    recv_msg = client_socket.recv(4096)
    print: recv_msg

    #send user details to server
    send_msg = input("Enter your user name(prefix with #):")
    send_msg = str.encode(send_msg)
    client_socket.send(send_msg)


    #receive and send message from/to different user/s

    while True:
        recv_msg = client_socket.recv(4096)
        print: recv_msg
        send_msg = input("Send your message in format [@user:message] ")
        if send_msg == 'exit':
            break
        else:
            client_socket.send(send_msg)

    client_socket.close()









