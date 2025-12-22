def generate_all_bytes():
    
    chars = []
    for i in range(0, 256):
        # print(f"\\x{i:02x}", end="")
        chars.append(f"\\x{i:02x}")
    return chars
    
print(generate_all_bytes())