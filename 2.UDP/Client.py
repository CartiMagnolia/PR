import socket
import threading

# adresa IP si portul serverului
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# initializarea socketului UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# cerem numele de utilizator
name = input("Introduceti numele de utilizator: ")
sock.sendto(name.encode("utf-8"), (UDP_IP, UDP_PORT))

# functia pentru citirea mesajelor de la server si afisarea acestora
def receive():
    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode("utf-8")
        print(message)

# pornim thread-ul de receptie
thread_recv = threading.Thread(target=receive)
thread_recv.start()

# citim mesajele de la tastatura si le trimitem catre server
while True:
    message = input("")
    if message.startswith("privat"):
        sock.sendto(message.encode("utf-8"), (UDP_IP, UDP_PORT))
    else:
        sock.sendto(f"{name}: {message}".encode("utf-8"), (UDP_IP, UDP_PORT))
