import socket

# Create a socket for communication with the master server
node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_address = ('master', 6000)  # Replace with the actual IP address of the master server

try:
    # Connect to the master server
    node_socket.connect(master_address)

    # Receive a message from the master
    data = node_socket.recv(1024).decode()
    print(f"Received message from the master: {data}")

finally:
    # Close the connection with the master
    node_socket.close()
