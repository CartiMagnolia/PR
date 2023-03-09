import socket
import threading

IP = 'localhost'
PORT = 5555

# cream un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# atasam adresa IP si portul la socketul serverului
server_socket.bind((IP, PORT))

# asteptam conexiuni
server_socket.listen()

print("SERVER ONLINE")

clients = []

def handle_client(client_socket, client_address):
    """
    Functia care gestioneaza mesajele de la un client
    """
    while True:
        try:
            # primim mesajul de la client
            message = client_socket.recv(1024)
            # printam mesajul si adresa clientului care l-a trimis
            print(f"{client_address}: {message.decode('utf-8')}")
            # retransmitem mesajul la toti clientii conectati, inclusiv cel care l-a trimis
            for c in clients:
                c.send(message)
        except:
            # in cazul in care avem o exceptie, inchidem conexiunea cu clientul si il eliminam din lista
            print(f"Conexiunea cu {client_address} s-a incheiat")
            clients.remove(client_socket)
            client_socket.close()
            break

while True:
    # asteptam conexiuni noi
    client_socket, client_address = server_socket.accept()
    # printam mesajul de conectare
    print(f"Conexiune noua de la {client_address}")
    # adaugam clientul la lista
    clients.append(client_socket)

    # pornim un thread pentru a gestiona mesajele de la clientul curent
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

