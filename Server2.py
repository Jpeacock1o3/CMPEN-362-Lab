from socket import *

# Step 1: Initialize the server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 8080))  # Bind to IP address and port 8080
serverSocket.listen(1)  # Listen for incoming connections

print("Server is ready to receive on port 8080")

while True:
    # Step 2: Establish a TCP connection
    connectionSocket, addr = serverSocket.accept()
    connectionSocket.settimeout(10)

    try:
        # Step 3: Receive HTTP request
        http_message = connectionSocket.recv(1024).decode()
        
        # Step 4: Parse the request to get the file name
        request_line = http_message.splitlines()[0]
        file_name = request_line.split()[1][1:]  # Extract the requested file

        # Step 5: Read the requested file from the server's file system
        try:
            with open(file_name, 'r') as f:
                file_content = f.read()

            # Step 6: Create HTTP response (200 OK)
            response = 'HTTP/1.1 200 OK\n\n' + file_content
        
        except IOError:
            # Step 6: File not found, send 404 Not Found
            response = 'HTTP/1.1 404 Not Found\n\n<html><body><h1>404 Not Found</h1></body></html>'
        
        # Step 7: Send the response
        connectionSocket.send(response.encode())
        
        # Step 8: Close the connection
        connectionSocket.close()

    except IOError:
        # Handling errors
        connectionSocket.close()

serverSocket.close()
