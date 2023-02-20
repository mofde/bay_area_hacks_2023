import socket
import threading
import datetime

# host and port
SERVER_ADDRESS = ('127.0.0.1', 12345)

# create a socket object and bind it to the server's address and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)

# function to handle client connections
def handle_client(client_socket, client_address):
    while True:
        # receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        # save the received data to a file
        with open('chat_history.txt', 'a') as file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f'{timestamp} {client_address}: {data}\n')
        # send the received data to all connected clients except the sender
        for sock, address in clients:
            if sock != client_socket:
                sock.sendall(f'{client_address}: {data}'.encode('utf-8'))

    # close the client socket and remove it from the list of clients
    clients.remove((client_socket, client_address))
    client_socket.close()

# create an empty list of clients
clients = []

# start listening for client connections
server_socket.listen()
print(f'Server is listening on {SERVER_ADDRESS}')
usernameInput = input("enter your username")
while True:
    # accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f'New client connected: {usernameInput}')
    # add the client socket and address to the list of clients
    clients.append((client_socket, client_address))
    # start a new thread to handle the client connection
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
