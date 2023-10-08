import socket

node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_address = ('master', 6000)  # Replace 'master' with the actual IP address of the master server

try:
    node_socket.connect(master_address)

    while True:
        message = input("Enter a message to send to the master (Q to quit): ").strip().upper()
        
        if message == 'Q':
            break
        
        if message == 'B':
            broadcast_message = input("Enter the broadcast message: ")
            node_socket.sendall(f"BROADCAST:{broadcast_message}".encode())
            response = node_socket.recv(1024).decode()
            print("Received response from master:", response)
        elif message == 'A':
            anycast_message = input("Enter the anycast message: ")
            node_socket.sendall(f"ANYCAST:{anycast_message}".encode())
            response = node_socket.recv(1024).decode()
            print("Received response from master:", response)

except KeyboardInterrupt:
    pass

finally:
    node_socket.close()

