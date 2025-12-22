import socket

IP = "127.0.0.1"
PORT = 5800
y = 100

while y < 3000:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    payload = "A" * y
    print(f"Fuzzing: Sending: {len(payload)} bytes")
    s.connect((IP, PORT))
    s.send(f"SEND {payload} \r\n".encode())
    s.recv(1024)
    y = y + 100