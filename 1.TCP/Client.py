import socket
import threading

# definim adresa IP si portul serverului
IP = 'localhost'
PORT = 5555

# cream un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ne conectam la server
client_socket.connect((IP, PORT))

def receive_messages():
    """
    Functia care primeste mesajele de la server si le afiseaza
    """
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Mesajul primit : {message}")
        except:
            # in cazul in care avem o exceptie, inchidem conexiunea cu serverul
            client_socket.close()
            break

# pornim un thread separat pentru a primi mesajele de la server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    # citim mesajul de la tastatura
    message = input()
    # trimitem mesajul la server
    client_socket.send(message.encode('utf-8'))
    if message.lower() == "bye":
        print("Aplicatia s-a inchis.")
        client_socket.send(message.encode('utf-8'))
        break
