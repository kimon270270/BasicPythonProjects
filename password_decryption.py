import base64

def decode_pass(password):
    decode_bytes=base64.b64decode(password)
    decode_data=decode_bytes.decode()
    print(f"Decoded password {decode_data}")

encode_string= input("Enter the base64 string: ")
decode_pass(encode_string)