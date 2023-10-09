import socket


# Create a socket for multicasting
multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

multicast_group = '224.1.1.1'
multicast_port = 6002

# Bind the multicast socket to the multicast group and port
multicast_socket.bind(('0.0.0.0', multicast_port))

# Join the multicast group
multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                            socket.inet_aton(multicast_group) + socket.inet_aton('0.0.0.0'))

# Create a socket for listening to incoming connections (TCP)
master_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master_address = ('0.0.0.0', 6000)

master_socket.bind(master_address)
master_socket.listen(4)

# List to store connected nodes' information
connected_nodes = []

while True:
    # Accept incoming connection from a node (TCP)
    node_socket, node_address = master_socket.accept()

    # Store information about the connected node
    connected_nodes.append((node_socket, node_address))

    # Send a message from the master to all connected nodes (TCP)
    message = "This is a message from the master to all nodes!"
    for node_sock, _ in connected_nodes:
        try:
            node_sock.sendall(message.encode())
        except BrokenPipeError:
            # Handle the BrokenPipeError (node closed the connection)
            node_sock.close()

    # Send a multicast message
    multicast_message = "This is a multicast message from the master!"
    multicast_socket.sendto(multicast_message.encode(), (multicast_group, multicast_port))
