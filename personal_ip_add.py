import socket

def find_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Your IP address is:", ip_address)

find_ip()
