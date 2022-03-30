import string
alphabet = list(string.ascii_lowercase)
binary_alphabet = [i.encode('utf-8') for i in alphabet]


def message_generator():
    logo_file = open(r"C:\Users\noase\Downloads\logo.jpg", "rb")
    data_byte = logo_file.read(1)
    while data_byte:
        code = ""
        while data_byte in binary_alphabet:
            code += data_byte.decode('utf-8')
            data_byte = logo_file.read(1)
        if len(code) > 4 and data_byte == b'!':
            code += "!"
            yield code
        data_byte = logo_file.read(1)


our_generator = message_generator()
print(next(our_generator))
print(next(our_generator))
print(next(our_generator))
print(next(our_generator))

