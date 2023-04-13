import socket

class DNSClient:
    def __init__(self):
        self.dns_server = socket.gethostbyname_ex(socket.gethostname())[2][0]

    def resolve(self, domain_or_ip):
        try:
            if domain_or_ip.replace(".", "").isnumeric():
                # For IP
                hostname = socket.gethostbyaddr(domain_or_ip)[0]
                ip_list = socket.gethostbyname_ex(hostname)[2]
                print(f"{hostname} este asociat cu adresa IP: {', '.join(ip_list)}")
            else:
                # For host
                ip_list = socket.gethostbyname_ex(domain_or_ip)[2]
                print(f"{domain_or_ip} este asociat cu adresele IP: {', '.join(ip_list)}")
        except socket.gaierror:
            print("Domeniu sau IP gresit")

    def use_dns(self, dns_ip):
        try:
            socket.gethostbyaddr(dns_ip)
            self.dns_server = dns_ip
            print(f"Utilizam: {dns_ip}")
        except socket.herror:
            print("Nu sa putut identifica serverul DNS specificat.")

    def get_dns_server(self):
        return self.dns_server

    print("Comenzile disponibile sunt:")
    print("  resolve <domain> sau resolve <ip> - afișează lista de IP-uri asignate domeniului sau invers")
    print("  use dns <ip> - schimba serverul DNS utilizat pentru rezolvarea numelor de domeniu")
    print("  get dns - afiseaza adresa IP a serverului DNS utilizat în prezent")

if __name__ == '__main__':
    client = DNSClient()

    while True:
        command = input("Introduceți o comanda: ")
        parts = command.split()

        if len(parts) == 2 and parts[0] == "resolve":
            client.resolve(parts[1])
        elif len(parts) == 3 and parts[0] == "use" and parts[1] == "dns":
            client.use_dns(parts[2])
        elif len(parts) == 2 and parts[0] == "get" and parts[1] == "dns":
            print(f"Serverul DNS utilizat în prezent este: {client.get_dns_server()}")
        else:
            print("Comanda nevalida. Comenzile disponibile sunt:")
            print("  resolve <domain> sau resolve <ip> - afișează lista de IP-uri asignate domeniului sau invers")
            print("  use dns <ip> - schimba serverul DNS utilizat pentru rezolvarea numelor de domeniu")
            print("  get dns - afiseaza adresa IP a serverului DNS utilizat în prezent")
