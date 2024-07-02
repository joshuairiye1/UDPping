import socket 
import time # Import time library
while True:
    print("\nChose your option to continue")
    print("----------------------------")
    print("1. Enter any key to ping to UDP server")
    print("2. Enter 0 to exit program")
    print("----------------------------\n")

    option = input("Enter your option:")
    if option == 0:
        break

    print("----------------------------")
    print("Starting Ping")
    print("----------------------------\n")

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a UDP socket for the client
    server_address = ('169.254.154.231', 1234) # Set IP Address and Port Number of Socket 
    mysocket.settimeout(2) # Sets a timeout value 2 seconds

    try: # Infinite loop to contiuously send messages to the server
        for i in range(0,4): 
            start = time.time() # Start time send message to server
            message = 'Ping ' +str(i) + " " + time.ctime()
            try:
                sent = mysocket.sendto(message.encode("utf-8"), server_address)
                print("Sent " + message)
                data, server = mysocket.recvfrom(1024) # Maximum data received 1024 bytes
                print("Received " + str(data))
                end = time.time()
                elapsed = end - start
                print("Time: " + str(elapsed * 1000) + " Milliseconds\n")
            except socket.timeout:
                print("#" + str(i) + " Requested Time out\n")
    finally:
        print("Finish ping, closing socket")
        mysocket.close()

