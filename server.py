from socket import *
import os

# Step 1: Initialize the socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 8080))  # Listen on all interfaces on port 8080
serverSocket.listen(1)
print('Server is ready to receive')

while True:
    # Step 2: Accept connections
    connectionSocket, addr = serverSocket.accept()
    print(f'Connection from {addr}')

    try:
        # Step 3: Receive and parse the request
        httpRequest = connectionSocket.recv(1024).decode()
        filename = httpRequest.split()[1][1:]  # Extract requested filename

        # Prevent directory traversal attacks by limiting file access to a known directory
        if ".." in filename or filename.startswith("/"):
            raise FileNotFoundError

        # Step 4: Read the requested file
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                content = f.read()
            header = 'HTTP/1.1 200 OK\n\n'
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        # Step 5: Handle 404 errors
        header = 'HTTP/1.1 404 Not Found\n\n'
        content = '<html><body><h1>404 Not Found</h1></body></html>'
    except Exception as e:
        # Handle any other errors and prevent server crashes
        header = 'HTTP/1.1 500 Internal Server Error\n\n'
        content = f'<html><body><h1>Internal Server Error</h1><p>{str(e)}</p></body></html>'

    # Step 6: Send the response and close the connection
    connectionSocket.sendall(header.encode() + content.encode())
    connectionSocket.close()
