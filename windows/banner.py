import socket

IP = "127.0.0.1"
PORT = 5800

def banner():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    banner = s.recv(1024)
    print(banner)
    s.send("HELP\r\n".encode())
    r = s.recv(1024)
    print(r.decode())
    
    
banner()