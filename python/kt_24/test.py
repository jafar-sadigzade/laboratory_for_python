import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('www.aztu.edu.az', 443))

client.send(b"GET / HTTP/1.0\r\nHost: 'www.aztu.edu.az\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response)
