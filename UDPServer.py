from socket import * # Import socket library
import random   # Import random library

serverSocket = socket(AF_INET, SOCK_DGRAM) # Create a UDP socket for the server
serverSocket.bind(('169.254.154.231', 1234)) # Set IP Address and Port Number of Socket
print("Started UDP Server IP Address: 169.254.154.231 and Port: 1234") # Print string on screen

while True: # Run program forever
    message, address = serverSocket.recvfrom(1234)
    message = message.upper() # Convert client message to uppercase letter
    serverSocket.sendto(message, address) # Send the uppercase message back to the client
