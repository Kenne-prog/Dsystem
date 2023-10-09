import socket

# Create a socket for listening to incoming connections
master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_address = ('0.0.0.0', 6000)  # Listen on all available network interfaces, port 6000

master_socket.bind(master_address)

# Listen for incoming connections (up to 4 nodes in this example)
master_socket.listen(4)

# List to store connected nodes' information
connected_nodes = []

# ...

while True:
    # Accept incoming connection from a node
    node_socket, node_address = master_socket.accept()

    # Store information about the connected node
    connected_nodes.append((node_socket, node_address))

    # Send a message from the master to all connected nodes
    message = "This is a message from the master to all nodes!"
    for node_sock, _ in connected_nodes:
        try:
            node_sock.sendall(message.encode())
        except BrokenPipeError:
            # Handle the BrokenPipeError (node closed the connection)
            node_sock.close()  # Close the socket