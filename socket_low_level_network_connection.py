# Creating a Simple TCP client 
import socket

TARGET_HOST = "example.com"
TARGET_PORT = 80
# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client.connect((TARGET_HOST,TARGET_PORT))
# Send Data
client.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
# Recieve Data
response = client.recv(4096)
# Print the response
print(response)