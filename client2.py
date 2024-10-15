from socket import *

# Step 1: Initialize a client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Step 2: Get a URI input from the user
uri = input('Enter the URI (e.g., http://127.0.0.1:8080/index.html): ')
host = uri.split('/')[2]  # Extract the host (IP address and port)
path = '/' + '/'.join(uri.split('/')[3:])  # Extract the path

# Step 3: Establish a TCP connection to the server
clientSocket.connect((host.split(':')[0], int(host.split(':')[1])))

# Step 4: Send HTTP GET request
http_request = f'GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n'
clientSocket.send(http_request.encode())

# Step 5: Receive and parse HTTP response
response = clientSocket.recv(1024).decode()

# Check if the response contains headers and body
if '\r\n\r\n' in response:
    headers, body = response.split('\r\n\r\n', 1)
else:
    headers = response
    body = ''

# Print headers and body (even if the body is empty)
print("Response Headers:", headers)
print("Body Content:", body)

# Step 6: Close the connection
clientSocket.close()
