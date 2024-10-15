from socket import *

# Step 1: Initialize the socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Step 2: Get the server address and file to request
server_host = '127.0.0.1'
server_port = 8080
requested_file = 'index.html'  # Modify this to request different files

try:
    # Step 3: Establish a connection to the server
    clientSocket.connect((server_host, server_port))

    # Step 4: Send an HTTP GET request
    request = f'GET /{requested_file} HTTP/1.1\r\nHost: {server_host}\r\n\r\n'
    clientSocket.send(request.encode())

    # Step 5: Receive the server's response
    response = clientSocket.recv(4096).decode()
    print(response)

except ConnectionError:
    print('Connection failed. Please ensure the server is running.')
finally:
    # Step 6: Close the connection
    clientSocket.close()
