import socket

# Create a socket for communication with the master server
node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_address = ('master', 6000)  # Replace with the actual IP address of the master server

try:
    # Connect to the master server
    node_socket.connect(master_address)

    # Send data to the master
    message = "BROADCAST:Hello from the node!"  
    node_socket.sendall(message.encode())

    # Receive a response from the master
    data = node_socket.recv(1024).decode()
    print(f"Received response from the master: {data}")

finally:
    # Close the connection with the master
    node_socket.close()
