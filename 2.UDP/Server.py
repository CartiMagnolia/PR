import socket

# adresa IP si portul serverului
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# initializarea socketului UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# dictionar pentru stocarea adreselor IP ale participantilor
clients = {}

print("Serverul de chat este pornit.")

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode("utf-8")

    # verificam daca adresa IP a unui participant exista in dictionar
    if addr not in clients.values():
        clients[message] = addr
        print(f"Participantul {message} s-a conectat.")
        sock.sendto("Te-ai conectat la serverul de chat.".encode("utf-8"), addr)
    else:
        # daca mesajul incepe cu "privat", trimitem mesajul doar catre participantul specificat
        if message.startswith("privat"):
            parts = message.split(":")
            dest_name = parts[1]
            dest_addr = clients[dest_name]
            msg = parts[2]
            sock.sendto(f"[privat] {msg}".encode("utf-8"), dest_addr)
        else:
            # in caz contrar, trimitem mesajul catre toti participantii
            for c in clients:
                sock.sendto(f"[general] {message}".encode("utf-8"), clients[c])
