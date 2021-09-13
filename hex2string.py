hexinput = input("Enter the hex code -> ")[2:]
bytes_obj = bytes.fromhex(hexinput)
readable = bytes_obj.decode("ASCII")
print(readable)
