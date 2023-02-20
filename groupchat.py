import socket
import threading

#socket setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#host and port
host = 'localhost'  #host?
port = 8000  #port?

server_socket.bind((host, port))

server_socket.listen()

# List to store connected clients
clients = []

# Function for client connections
def handle_client(client_socket, client_address):
    print(f"Connected: {client_address}")

    # Add client to list of connected clients
    clients.append(client_socket)

    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)

            # Broadcast message to all connected clients
            for client in clients:
                client.send(message)

        except:
            #error
            clients.remove(client_socket)
            client_socket.close()
            print(f"Disconnected: {client_address}")
            break

#start the server function
def start_server():
    print(f"Server started on {host}:{port}")

    while True:
        # Wait for incoming connection
        client_socket, client_address = server_socket.accept()

        # Start a new thread to handle the connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    start_server()

print(debugger=true)