import socket
from Crypto.PublicKey import ECC

key = ECC.generate(curve='P-256')


keys = f"{key.public_key().export_key(format='PEM')}\r\n\r\n{key.export_key(format='PEM')}"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.0.69.85', 1337))
s.recv(10000)
s.sendall(keys.encode())
response = s.recv(10000).decode()
print(response)