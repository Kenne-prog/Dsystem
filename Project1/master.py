import socket

# Create a socket for listening to incoming connections
master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_address = ('0.0.0.0', 6000)  # Listen on all available network interfaces, port 6000

master_socket.bind(master_address)

# Listen for incoming connections (up to 4 nodes in this example)
master_socket.listen(4)

# List to store connected nodes' information
connected_nodes = []

while True:
    # Accept incoming connection from a node
    node_socket, node_address = master_socket.accept()

    # Store information about the connected node
    connected_nodes.append((node_socket, node_address))

    # Receive data from the node
    data = node_socket.recv(1024).decode()
    print(f"Received data from node: {data}")

    # Determine if it's a broadcast or anycast message based on the data
    if data.startswith("BROADCAST:"):
        # Broadcast message, send it to all connected nodes
        broadcast_message = data[len("BROADCAST:"):]
        for node_sock, _ in connected_nodes:
            node_sock.sendall(broadcast_message.encode())
    elif data.startswith("ANYCAST:"):
        # Anycast message, determine the nearest node and route it
        anycast_message = data[len("ANYCAST:"):]
        # Implement logic to find the nearest node and route the message

    # Close the connection with the node (no need to close it here)
    # node_socket.close()
