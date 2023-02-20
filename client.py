import socket
import threading

# host and port
SERVER_ADDRESS = ('127.0.0.1', 12345)

# creating a socket object and connecting it to the server's host and port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)

# function to handle incoming messages from the server
def handle_messages():
    while True:
        # receive data from the server
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(data)

# start a new thread to handle incoming messages from the server
threading.Thread(target=handle_messages).start()

# loop to send messages to the server
while True:
    message = input('> ')
    if message:
        # send the message to the server
        client_socket.sendall(message.encode('utf-8'))
