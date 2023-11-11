import socket
from threading import Thread

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def acceptConnections():
    global SERVER
    global clients
    
    while True:
        client, addr = SERVER.accept()
        client_name = SERVER.recv(4096).decode.lower()
        clients[client_name] = {
            "client": client,
            "address": addr,
            "connected_with": "",
            "file_name": "",
            "file_size": 4096
        }
        print(f"Connection established with {client_name}: {addr}")

        thread = Thread(target=handleClient, args=(client, client_name,))
        thread.start()

def setup():
    print("\n\t\t\t\t\tMusic Sharing App\n")

    # getting global values
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    # listening to incoming connections (max 100)
    SERVER.listen(100)

    print("\t\t\t\tWaiting for incoming connections...\n")

    acceptConnections()

# using thread to accpet and deal with all requests simultaneously
setup_thread = Thread(target=setup)
setup_thread.start()